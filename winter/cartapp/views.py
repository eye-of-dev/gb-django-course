from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
import uuid

from shop.models import Products

from cartapp.models import Cart


def index_view(request):
    """ Корзина
    :param request:
    :return:
    """

    cart = Cart.objects.filter(cart_uuid=request.COOKIES.get('cart_uuid')).all()

    content = {
        'title': 'корзина',
        'cart': cart
    }
    return render(request, 'cart.html', content)


def add_view(request, pk):
    """
    Добавления товара в корзину
    todo Генерацю и получения cart_uuid вывести в общий контроллер. тема будет рассматриваться на последнем уроке
    todo пока не хватает знаний(:
    :param request:
    :param pk:
    :return:
    """
    cart_uuid = request.COOKIES.get('cart_uuid')
    if cart_uuid is None:
        cart_uuid = uuid.uuid1()

    product = get_object_or_404(Products, pk=pk)
    cart = Cart.objects.filter(cart_uuid=cart_uuid, product=product).first()

    if not cart:
        if request.user.is_authenticated:
            cart = Cart(cart_uuid=cart_uuid, user=request.user, product=product)
        else:
            cart = Cart(cart_uuid=cart_uuid, product=product)

    cart.quantity += 1
    cart.price = product.price
    cart.save()

    response = redirect(request.META.get('HTTP_REFERER'))
    response.set_cookie('cart_uuid', value=cart_uuid, max_age=30 * 24 * 60 * 60)
    return response


def update_view(request):
    pass


def delete_view(request):
    pass


def checkout_view(request):
    pass


def get_cart_uuid(request):
    response = HttpResponse("Cart uuid")

    cart_uuid = request.COOKIES.get('cart_uuid')
    if cart_uuid is None:
        response.set_cookie('cart_uuid', uuid.uuid1())

    return response
