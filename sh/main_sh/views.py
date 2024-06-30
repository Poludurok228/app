from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from cat.models import Asic
from .models import *
from .forms import *
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.translation import gettext_lazy as _


def home_page(request):

    asic = Asic.popularity.all().order_by('asic_number')
    slide = Slide.main_slide.all()
    review = Reviews.objects.all()
    steps = OrderSteps.objects.all()

    context = {
        'asic': asic,
        'slide': slide,
        'review': review,
        'steps': steps,
    }

    return render(request, 'main_sh/home.html', context)


def blog_page(request):

    news = BlogNews.published.all()
    form = BlogForm()

    if request.method == 'POST':
        form = BlogForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']

            context = {
                'name': name,
                'phone': phone
            }

            html_body = render_to_string('main_sh/mail_body1.html', context)

            mail = EmailMessage(
                subject='Заявка',
                body=html_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=['crypto.tech@mail.ru']
            )

            mail.content_subtype = 'html'
            mail.send()

            return redirect('catalog:thanks')

    paginator = Paginator(news, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    favorites_slugs = request.session.get('favorites', [])
    favorites_asics = Asic.objects.filter(slug__in=favorites_slugs)
    favourites_count = favorites_asics.count()

    context = {
        'page_obj': page_obj,
        'favourites_count': favourites_count,
        'form': form,
    }

    return render(request, 'main_sh/blog.html', context)


def detail_news(request, slug):

    news = get_object_or_404(BlogNews, slug=slug)
    tags = news.tegs.all()
    favorites_slugs = request.session.get('favorites', [])
    favorites_asics = Asic.objects.filter(slug__in=favorites_slugs)
    favourites_count = favorites_asics.count()

    same_news = BlogNews.objects.filter(tegs__in=tags).exclude(id=news.id).distinct()[:3]

    context = {
        'news': news,
        'same_news': same_news,
        'favourites_count': favourites_count,
    }

    return render(request, 'main_sh/detail_news.html', context)


def detail_tags(request, slug):

    tags = get_object_or_404(BlogTag, slug=slug)
    news = BlogNews.published.filter(tegs=tags)
    form = BlogForm()

    paginator = Paginator(news, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    favorites_slugs = request.session.get('favorites', [])
    favorites_asics = Asic.objects.filter(slug__in=favorites_slugs)
    favourites_count = favorites_asics.count()

    context = {
        'page_obj': page_obj,
        'favourites_count': favourites_count,
        'form': form,
    }

    return render(request, 'main_sh/blog.html', context)


def check_order(request):

    if 'q_order' in request.GET:
        q = request.GET['q_order']

        try:
            order = Order.objects.get(order_number__iexact=q)
            return render(request, 'main_sh/order.html', {'order': order})
        except Order.DoesNotExist:
            wrong = _('Заказ не найден, проверьте номер заказа и попробуйте снова.')

            return render(request, 'main_sh/order.html', {'wrong': wrong})

    return render(request, 'main_sh/order.html')


def check_warranty(request):

    if 'q_warranty' in request.GET:
        q = request.GET['q_warranty']

        try:
            warranty = Warranty.objects.get(art__iexact=q)
            return render(request, 'main_sh/warranty.html', {'warranty': warranty})
        except Warranty.DoesNotExist:
            wrong = _('Гарантия не найдена, проверьте номер гарантии и попробуйте снова.')
            return render(request, 'main_sh/warranty.html', {'wrong': wrong})

    return render(request, 'main_sh/warranty.html')


def about_us(request):

    news_tag = BlogTag.objects.all()[:8]
    step = AboutSteps.objects.all()
    trust = TrustSteps.objects.all()
    photo = PhotoLocation.objects.all()

    if request.method == 'POST':
        form1 = CodForm1(request.POST)

        if form1.is_valid():
            name = form1.cleaned_data['name']
            contact = form1.cleaned_data['contact']

            context = {
                'name': name,
                'contact': contact,
            }

            html_body = render_to_string('main_sh/mail_body1.html', context)

            mail = EmailMessage(
                subject='Заявка ЦОД 1',
                body=html_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=['crypto.tech@mail.ru']
            )

            mail.content_subtype = 'html'
            mail.send()

            return redirect('main_page:about')
    else:
        form1 = CodForm1()

    if request.method == 'POST':
        form2 = CodForm2(request.POST)

        if form1.is_valid():
            name = form2.cleaned_data['name']
            contact = form2.cleaned_data['contact']

            context = {
                'name': name,
                'contact': contact,
            }

            html_body = render_to_string('main_sh/mail_body2.html', context)

            mail = EmailMessage(
                subject='Заявка ЦОД 2',
                body=html_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=['crypto.tech@mail.ru']
            )

            mail.content_subtype = 'html'
            mail.send()

            return redirect('main_page:about')
    else:
        form2 = CodForm2()


    context = {
        'news_tag': news_tag,
        'step': step,
        'trust': trust,
        'form1': form1,
        'form2': form2,
        'photo': photo,
    }

    return render(request, 'main_sh/about.html', context)


def placement(request):
    favorites_slugs = request.session.get('favorites', [])
    favorites_asics = Asic.objects.filter(slug__in=favorites_slugs)
    favourites_count = favorites_asics.count()

    context = {
        'favourites_count': favourites_count
    }

    return render(request, 'main_sh/razmecenie.html', context)


def map_page(request):
    favorites_slugs = request.session.get('favorites', [])
    favorites_asics = Asic.objects.filter(slug__in=favorites_slugs)
    favourites_count = favorites_asics.count()
    form = BlogForm()

    context = {
        'favourites_count': favourites_count,
        'form': form
    }

    return render(request, 'main_sh/map.html', context)


def download_file(request):
    latest_file = UploadFile.objects.first()
    file_path = latest_file.file.path

    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=' + latest_file.title
        return response


def contracts(request):
    contract = Contracts.objects.filter(contract_number=1)
    form = BlogForm()

    favorites_slugs = request.session.get('favorites', [])
    favorites_asics = Asic.objects.filter(slug__in=favorites_slugs)
    favourites_count = favorites_asics.count()

    context = {
        'con': contract,
        'favourites_count': favourites_count,
        'form': form,
    }

    return render(request, 'main_sh/contracts.html', context=context)


def contract_2(request):
    contract = Contracts.objects.filter(contract_number=2)
    form = BlogForm()

    favorites_slugs = request.session.get('favorites', [])
    favorites_asics = Asic.objects.filter(slug__in=favorites_slugs)
    favourites_count = favorites_asics.count()

    context = {
        'con': contract,
        'favourites_count': favourites_count,
        'form': form,
    }

    return render(request, 'main_sh/contracts.html', context=context)


def contract_3(request):
    contract = Contracts.objects.filter(contract_number=3)
    form = BlogForm()

    favorites_slugs = request.session.get('favorites', [])
    favorites_asics = Asic.objects.filter(slug__in=favorites_slugs)
    favourites_count = favorites_asics.count()

    context = {
        'con': contract,
        'favourites_count': favourites_count,
        'form': form,
    }

    return render(request, 'main_sh/contracts.html', context=context)


def contract_4(request):
    contract = Contracts.objects.filter(contract_number=4)
    form = BlogForm()

    favorites_slugs = request.session.get('favorites', [])
    favorites_asics = Asic.objects.filter(slug__in=favorites_slugs)
    favourites_count = favorites_asics.count()

    context = {
        'con': contract,
        'favourites_count': favourites_count,
        'form': form,
    }

    return render(request, 'main_sh/contracts.html', context=context)


def sorry(request):
    return render(request, 'main_sh/sorry.html')















