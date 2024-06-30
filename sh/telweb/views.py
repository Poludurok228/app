from decimal import Decimal
import math
from django.contrib import messages

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.db import transaction
from main_sh.models import Order, OrderLot, Shipping, Application
from cat.models import AsicBrand, Asic
import random
from .models import *
from django.utils import timezone


USD = Decimal('94.5')


def index(request):

    return render(request, 'telweb/home.html')


def brand_cat(request):

    brands = AsicBrand.objects.all()

    context = {
        'brand': brands,
    }

    return render(request, 'telweb/brend_cat.html', context)


def brand_detail(request, slug):
    brands = get_object_or_404(AsicBrand, slug=slug)
    asic = Asic.objects.filter(brand=brands)
    asic_count = asic.count()

    basket = request.session.get('basket', {})
    unique_basket_item_count = len(basket)

    context = {
        'brand': brands,
        'asic': asic,
        'asic_count': asic_count,
        'basket_item_count': unique_basket_item_count,
    }

    return render(request, 'telweb/catalog.html', context)


def init_basket(request):
    basket = request.session.get('basket', {})
    if not basket:
        request.session['basket'] = {}


def add_to_basket(request, asic_id):
    init_basket(request)
    basket = request.session['basket']
    basket[str(asic_id)] = basket.get(str(asic_id), 0) + 1
    request.session.modified = True

    referer_url = request.META.get('HTTP_REFERER')

    return HttpResponseRedirect(referer_url if referer_url else '/')


def remove_single_from_basket(request, asic_id):
    basket = request.session.get('basket', {})
    if str(asic_id) in basket:
        if basket[str(asic_id)] > 1:
            basket[str(asic_id)] -= 1
        else:
            del basket[str(asic_id)]
        request.session.modified = True

    referer_url = request.META.get('HTTP_REFERER')

    return HttpResponseRedirect(referer_url if referer_url else '/')


def remove_all_from_basket(request, asic_id):
    basket = request.session.get('basket', {})
    if str(asic_id) in basket:
        del basket[str(asic_id)]
        request.session.modified = True

    referer_url = request.META.get('HTTP_REFERER')

    return HttpResponseRedirect(referer_url if referer_url else '/')


def clear_basket(request):
    request.session['basket'] = {}
    request.session.modified = True


def basket_page(request):
    basket = request.session.get('basket', {})
    items = []
    total_price = 0
    basket_item_count = sum(basket.values())

    for asic_id, quantity in basket.items():
        asic = Asic.objects.get(id=asic_id)  #
        total_price += asic.price * quantity
        items.append({
            'asic': asic,
            'quantity': quantity,
            'subtotal': asic.price * quantity
        })

    context = {
        'basket_items': items,
        'total_price': total_price,
        'basket_item_count': basket_item_count,
    }

    return render(request, 'telweb/basket.html', context)


def pay(request):
    basket = request.session.get('basket', {})

    def generate_random_number():
        return random.randint(1000000000, 9999999999)

    def generate_unique_order_number():
        while True:
            order_number_generated = generate_random_number()
            if not Order.objects.filter(order_number=order_number_generated).exists():
                break
        return order_number_generated

    last_order_number = request.session.get('last_order_number', Order.objects.count())
    order_title = f'Заказ №{last_order_number + 1}'
    request.session['last_order_number'] = last_order_number + 1

    if not basket:
        return redirect('telegram:brand_cat')

    basket_items = []
    total_price = Decimal(0)
    total_price_usdt = Decimal(0)

    for asic_id, quantity in basket.items():
        try:
            asic = Asic.objects.get(id=asic_id)
            price = asic.usdt * quantity * USD
            usdt_price = asic.usdt * quantity
            percent_price = math.ceil(price / 100) * 100
            basket_items.append({
                'asic': asic,
                'quantity': quantity,
                'total_item_price': round(percent_price, 0),
                'total_item_price_usdt': round(usdt_price, 0),
            })
            total_price += price
            total_price_usdt += usdt_price
        except Asic.DoesNotExist:
            continue

    total_order_price = sum(item['total_item_price'] for item in basket_items)
    total_order_price_usdt = sum(item['total_item_price_usdt'] for item in basket_items)
    referer_url = request.META.get('HTTP_REFERER', '/')
    order_number_g = generate_unique_order_number()

    context = {
        'basket_items': basket_items,
        'total_price': total_price,
        'referer_url': referer_url,
        'total_order_price': total_order_price,
        'total_order_price_usdt': round(total_price_usdt, 0),
        'order_number': order_number_g
    }

    if request.method == "POST":
        field_names = {
            'payment_way': 'Способ оплаты',
            'get_way': 'Способ получения',
            'recipient_name': 'Имя получателя',
            'phone': 'Телефон'
        }

        required_fields = ['payment_way', 'get_way', 'recipient_name', 'phone']
        missing_fields = []

        for field in required_fields:
            if not request.POST.get(field):
                missing_fields.append(field)

        if missing_fields:
            for field in missing_fields:
                messages.error(request, f'Поле "{field_names.get(field, field)}" обязательно для заполнения.')
        else:
            shipping = Shipping(
                payment_way=request.POST.get('payment_way'),
                get_way=request.POST.get('get_way'),
                address=request.POST.get('delivery_address', '') if request.POST.get('get_way') == 'delivery' else '',
                recipient_name=request.POST.get('recipient_name'),
                phone=request.POST.get('phone'),
                comment=request.POST.get('comment', '')
            )
            shipping.save()

            order = Order.objects.create(
                title=order_title,
                total_price=total_order_price,
                shipping=shipping,
                order_number=order_number_g,
            )

            for item in basket_items:
                order_lot = OrderLot.objects.create(
                    title=f'Лот {OrderLot.objects.count() + 1}',
                    asic=item['asic'],
                    quantity=item['quantity'],
                    total_price=item['total_item_price'],
                )
                order.order_lots.add(order_lot)

            application = Application.objects.create(order=order)

            request.session['basket'] = {}
            request.session['application_id'] = application.id
            request.session['order_number'] = order.order_number

            if request.POST.get('payment_way') == 'usdt_self':
                return redirect('telegram:choice_network')
            else:
                return redirect('telegram:solo_page')

    return render(request, 'telweb/pay_page.html', context)


def choice_network(request):

    net = WalletUSDT.objects.all()

    return render(request, 'telweb/pay_choise.html', {'net': net})


def solo_page(request):
    order_number = request.session.get('order_number')
    context = {'order_number': order_number}

    return render(request, 'telweb/not_solo.html', context)


def net_detail(request, slug):
    net = get_object_or_404(WalletUSDT, slug=slug)
    basket = request.session.get('basket', {})

    application_id = request.session.get('application_id')

    expiry_time = None

    if application_id is not None:
        application = Application.objects.filter(id=application_id).first()
        if application:
            order_number = application.order.order_number
            total = application.order.total_price
            # Округляем до ближайших 50 вниз
            total_price = math.floor(round(total / Decimal(USD), 0) / 50) * 50
            expiry_time = application.created_at + timezone.timedelta(minutes=60)
            if timezone.now() < expiry_time:
                fl = True
            else:
                fl = False
        else:
            expiry_time = "Заявка не найдена или время истечения не определено."
            order_number = ''
            total_price = ''
            fl = False
    else:
        expiry_time = "Идентификатор заявки не найден."
        order_number = ''
        total_price = ''
        fl = False
        application = ''

    context = {
        'net': net,
        'expiry_time': expiry_time,
        'order_number': order_number,
        'total_price': total_price,
        'fl': fl,
        'application': application,
    }

    return render(request, 'telweb/net_detail.html', context)
