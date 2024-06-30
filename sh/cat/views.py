from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Min, Max, Q
from .models import *
from .forms import *
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from urllib.parse import urlencode
from django.contrib import messages


GRIVNA = Decimal('0.305')


def send_custom_email(subject, body, recipients):
    email = EmailMessage(
        subject=subject,
        body=body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=recipients
    )
    email.content_subtype = 'html'
    email.send()


def catalog_page(request):

    brand = AsicBrand.objects.all()
    coin = Coin.objects.all()

    favorites_slugs = request.session.get('favorites', [])
    favorites_asics = Asic.objects.filter(slug__in=favorites_slugs)
    favourites_count = favorites_asics.count()

    global_min_price = Asic.published.aggregate(Min('usdt'))['usdt__min']
    global_max_price = Asic.published.aggregate(Max('usdt'))['usdt__max']

    global_min_power = Asic.published.aggregate(Min('power'))['power__min']
    global_max_power = Asic.published.aggregate(Max('power'))['power__max']

    asic = Asic.published.all()

    min_price = request.GET.get('min_price', None)
    max_price = request.GET.get('max_price', None)

    min_power = request.GET.get('min_power', None)
    max_power = request.GET.get('max_power', None)

    brands = request.GET.getlist('brand')
    coins = request.GET.getlist('coin')

    coin_param = request.GET.get('ff_coin', None)

    if 'q' in request.GET:
        q = request.GET['q']
        asic = Asic.published.filter(title__icontains=q)
    else:
        asic = Asic.published.all()

    if min_price is not None:
        min_price = float(min_price)
        if min_price != global_min_price:
            asic = asic.filter(usdt__gte=min_price)

    if max_price is not None:
        max_price = float(max_price)
        if max_price != global_max_price:
            asic = asic.filter(usdt__lte=max_price)

    if brands:
        brands = [int(brand_id) for brand_id in brands if brand_id.isdigit()]
        asic = asic.filter(brand__id__in=brands)

    if coins:
        coins = [int(coin_id) for coin_id in coins if coin_id.isdigit()]
        asic = asic.filter(coin__id__in=coins)

    if min_power is not None:
        min_power = float(min_power)
        if min_power != global_min_power:
            asic = asic.filter(power__gte=min_power)

    if max_power is not None:
        max_power = float(max_power)
        if max_power != global_max_power:
            asic = asic.filter(power__lte=max_power)

    if coin_param:
        try:
            coin_param = str(coin_param)
            asic = asic.filter(coin__title=coin_param)
        except ValueError:
            pass

    paginator = Paginator(asic, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    nothing = asic.count() == 0

    fs_filters = FastFilter.objects.all()

    filter_params = {
        'min_price': min_price,
        'max_price': max_price,
        'min_power': min_power,
        'max_power': max_power,
        'brand': brands,
        'coin': coins,
    }

    filter_params = {k: v for k, v in filter_params.items() if v is not None}

    query_string = urlencode(filter_params, doseq=True)

    context = {
        'asic': asic,
        'brand': brand,
        'coin': coin,
        'count': asic.count(),
        'min': global_min_price,
        'max': global_max_price,
        'p_min': global_min_power,
        'p_max': global_max_power,
        'nothing': nothing,
        'fs_fl': fs_filters,
        'page_obj': page_obj,
        'query_string': query_string,
        'favourites_count': favourites_count,
    }

    return render(request, 'cat/home.html', context=context)


def brand_detail(request, slug):

    brand = AsicBrand.objects.all()
    brand2 = get_object_or_404(AsicBrand, slug=slug)
    asic = Asic.published.filter(brand=brand2)

    paginator = Paginator(asic, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    favorites_slugs = request.session.get('favorites', [])
    favorites_asics = Asic.objects.filter(slug__in=favorites_slugs)
    favourites_count = favorites_asics.count()

    asic_count = asic.count()

    fs_filters = FastFilter.objects.all()

    global_min_price = Asic.published.aggregate(Min('usdt'))['usdt__min']
    global_max_price = Asic.published.aggregate(Max('usdt'))['usdt__max']

    global_min_power = Asic.published.aggregate(Min('power'))['power__min']
    global_max_power = Asic.published.aggregate(Max('power'))['power__max']

    nothing = asic.count() == 0

    context = {
        'asic': asic,
        'brand': brand,
        'count': asic_count,
        'min': global_min_price,
        'max': global_max_price,
        'p_min': global_min_power,
        'p_max': global_max_power,
        'nothing': nothing,
        'fs_fl': fs_filters,
        'page_obj': page_obj,
        'favourites_count': favourites_count
    }

    return render(request, 'cat/home.html', context=context)


def asic_detail(request, slug):
    asic = get_object_or_404(Asic, slug=slug)

    # Initialize all forms, regardless of the request type initially once
    form = TabsForm(request.POST or None)
    form2 = QuestionAsicForm(request.POST or None)
    form3 = OrderForm(request.POST or None)

    favorites_slugs = request.session.get('favorites', [])
    is_favorite = slug in favorites_slugs
    favorites_asics = Asic.objects.filter(slug__in=favorites_slugs)
    favourites_count = favorites_asics.count()

    if request.method == 'POST':
        if 'order_form' in request.POST and form3.is_valid():
            name = form3.cleaned_data['name']
            phone = form3.cleaned_data['phone']
            email = form3.cleaned_data['email']
            telegram = form3.cleaned_data['telegram']
            quantity = request.POST.get('totality_quantity')
            price = request.POST.get('totality_price')
            context = {'name': name, 'phone': phone, 'email': email, 'telegram': telegram, 'quantity': quantity, 'price': price, 'asic': asic,}
            html_o_body = render_to_string('cat/detail_mail.html', context)
            send_custom_email('Заявка Detail', html_o_body, ['crypto.tech@mail.ru'])
            return redirect('catalog:thanks')

        elif 'tabs_form' in request.POST and form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            context = {'asic': asic, 'name': name, 'phone': phone}
            html_body = render_to_string('cat/feedback.html', context)
            send_custom_email('Новая заявка на обратную связь', html_body,
                              ['crypto.tech@mail.ru'])
            return redirect('catalog:thanks')

        elif 'question_form' in request.POST and form2.is_valid():
            context = {
                'name': form2.cleaned_data['name'],
                'mail': form2.cleaned_data['mail'],
                'contact': form2.cleaned_data['contact'],
                'message': form2.cleaned_data['message'],
                'asic': asic,
            }
            html_q_body = render_to_string('cat/question_mail.html', context)
            send_custom_email(form2.cleaned_data['sub'], html_q_body, ['crypto.tech@mail.ru'])
            return redirect('catalog:thanks')

    # Forms are already initialized, simply reconstruct the context
    context = {
        'asic': asic,
        'form': form,
        'form2': form2,
        'form3': form3,
        'is_favorite': is_favorite,
        'favourites_count': favourites_count
    }

    return render(request, 'cat/detail.html', context=context)


def power_asic(request):

    asic = Asic.published.filter(price__gt=400000)
    brand = AsicBrand.objects.all()

    paginator = Paginator(asic, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    favorites_slugs = request.session.get('favorites', [])
    favorites_asics = Asic.objects.filter(slug__in=favorites_slugs)
    favourites_count = favorites_asics.count()

    asic_count = asic.count()

    fs_filters = FastFilter.objects.all()

    global_min_price = Asic.published.aggregate(Min('usdt'))['usdt__min']
    global_max_price = Asic.published.aggregate(Max('usdt'))['usdt__max']

    global_min_power = Asic.published.aggregate(Min('power'))['power__min']
    global_max_power = Asic.published.aggregate(Max('power'))['power__max']

    nothing = asic.count() == 0

    context = {
        'asic': asic,
        'brand': brand,
        'count': asic_count,
        'min': global_min_price,
        'max': global_max_price,
        'p_min': global_min_power,
        'p_max': global_max_power,
        'nothing': nothing,
        'fs_fl': fs_filters,
        'page_obj': page_obj,
        'favourites_count': favourites_count,
    }

    return render(request, 'cat/home_fast_settings.html', context=context)


def add_to_favorites(request, slug):

    favorites = request.session.get('favorites', [])
    if slug not in favorites:
        favorites.append(slug)
        request.session['favorites'] = favorites
        messages.info(request, 'Асик успешно добавлен в избранное!')
    else:
        messages.error(request, 'Асик уже находится в вашем списке избранного!')
    return redirect('catalog:asic_detail', slug=slug)


def favorites_page(request):

    favorites_slugs = request.session.get('favorites', [])
    favorites_asics = Asic.objects.filter(slug__in=favorites_slugs)
    favourites_count = favorites_asics.count()

    context = {
        'favourites_count': favourites_count,
        'favorites_asics': favorites_asics
    }

    return render(request, 'cat/faivorit.html', context)


def stabilizer_page(request):

    brand = StabilizerBrand.objects.all()

    if 'q_stab' in request.GET:
        q = request.GET['q_stab']
        stab = Stabilizer.objects.filter(title__icontains=q)
        stab_count = stab.count()
    else:
        stab = Stabilizer.objects.all()
        stab_count = stab.count()

    favorites_slugs = request.session.get('favorites', [])
    favorites_asics = Asic.objects.filter(slug__in=favorites_slugs)
    favourites_count = favorites_asics.count()

    context = {
        'stab': stab,
        'brand': brand,
        'favourites_count': favourites_count,
        'stab_count': stab_count,
    }

    return render(request, 'cat/home_stab.html', context)


def stabilizer_detail(request, slug):

    stab = get_object_or_404(Stabilizer, slug=slug)

    favorites_slugs = request.session.get('favorites', [])
    favorites_asics = Asic.objects.filter(slug__in=favorites_slugs)
    favourites_count = favorites_asics.count()

    form = TabsForm(request.POST or None)
    form2 = QuestionAsicForm(request.POST or None)
    form3 = OrderForm(request.POST or None)

    if request.method == 'POST':
        if 'order_form' in request.POST and form3.is_valid():
            name = form3.cleaned_data['name']
            phone = form3.cleaned_data['phone']
            email = form3.cleaned_data['email']
            telegram = form3.cleaned_data['telegram']
            quantity = request.POST.get('totality_quantity')
            price = request.POST.get('totality_price')
            context = {'name': name, 'phone': phone, 'email': email, 'telegram': telegram, 'quantity': quantity, 'price': price, 'asic': stab,}
            html_o_body = render_to_string('cat/detail_mail.html', context)
            send_custom_email('Заявка Detail', html_o_body, ['crypto.tech@mail.ru'])
            return redirect('catalog:thanks')

        elif 'tabs_form' in request.POST and form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            context = {'asic': stab, 'name': name, 'phone': phone}
            html_body = render_to_string('cat/feedback.html', context)
            send_custom_email('Новая заявка на обратную связь', html_body,
                              ['crypto.tech@mail.ru'])
            return redirect('catalog:thanks')

        elif 'question_form' in request.POST and form2.is_valid():
            context = {
                'name': form2.cleaned_data['name'],
                'mail': form2.cleaned_data['mail'],
                'contact': form2.cleaned_data['contact'],
                'message': form2.cleaned_data['message'],
                'asic': stab,
            }
            html_q_body = render_to_string('cat/question_mail.html', context)
            send_custom_email(form2.cleaned_data['sub'], html_q_body, ['crypto.tech@mail.ru'])
            return redirect('catalog:thanks')

    context = {
        'stab': stab,
        'favourites_count': favourites_count,
        'form': form,
        'form2': form2,
        'form3': form3,
    }

    return render(request, 'cat/detail_stabilizer.html', context)


def stabilizer_brand_detail(request, slug):

    brand_l = get_object_or_404(StabilizerBrand, slug=slug)
    brand = StabilizerBrand.objects.all()
    stab = Stabilizer.objects.filter(brand=brand_l)

    favorites_slugs = request.session.get('favorites', [])
    favorites_asics = Asic.objects.filter(slug__in=favorites_slugs)
    favourites_count = favorites_asics.count()
    stab_count = stab.count()

    context = {
        'brand': brand,
        'stab': stab,
        'favourites_count': favourites_count,
        'stab_count': stab_count,
    }

    return render(request, 'cat/home_stab.html', context)


def stabilizer_one_phase(request):

    brand = StabilizerBrand.objects.all()
    stab = Stabilizer.objects.filter(phase_id=1)

    favorites_slugs = request.session.get('favorites', [])
    favorites_asics = Asic.objects.filter(slug__in=favorites_slugs)
    favourites_count = favorites_asics.count()
    stab_count = stab.count()

    nothing = stab.count() == 0

    context = {
        'brand': brand,
        'stab': stab,
        'favourites_count': favourites_count,
        'stab_count': stab_count,
        'nothing': nothing,
    }

    return render(request, 'cat/home_stab.html', context)


def stabilizer_three_phase(request):
    brand = StabilizerBrand.objects.all()
    stab = Stabilizer.objects.filter(phase_id=2)

    favorites_slugs = request.session.get('favorites', [])
    favorites_asics = Asic.objects.filter(slug__in=favorites_slugs)
    favourites_count = favorites_asics.count()
    stab_count = stab.count()

    nothing = stab.count() == 0

    context = {
        'brand': brand,
        'stab': stab,
        'favourites_count': favourites_count,
        'stab_count': stab_count,
        'nothing': nothing,
    }

    return render(request, 'cat/home_stab.html', context)


def stabilizer_low_price(request):
    brand = StabilizerBrand.objects.all()
    stab = Stabilizer.objects.order_by('-price')

    favorites_slugs = request.session.get('favorites', [])
    favorites_asics = Asic.objects.filter(slug__in=favorites_slugs)
    favourites_count = favorites_asics.count()
    stab_count = stab.count()

    nothing = stab.count() == 0

    context = {
        'brand': brand,
        'stab': stab,
        'favourites_count': favourites_count,
        'stab_count': stab_count,
        'nothing': nothing,
    }

    return render(request, 'cat/home_stab.html', context)


def stabilizer_max_price(request):
    brand = StabilizerBrand.objects.all()
    stab = Stabilizer.objects.order_by('price')

    favorites_slugs = request.session.get('favorites', [])
    favorites_asics = Asic.objects.filter(slug__in=favorites_slugs)
    favourites_count = favorites_asics.count()
    stab_count = stab.count()

    nothing = stab.count() == 0

    context = {
        'brand': brand,
        'stab': stab,
        'favourites_count': favourites_count,
        'stab_count': stab_count,
        'nothing': nothing,
    }

    return render(request, 'cat/home_stab.html', context)


def thanks(request):
    referer_url = request.META.get('HTTP_REFERER')

    return render(request, 'cat/thanks.html', {'referer_url': referer_url})
