from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
import uuid

from shop.models import Products

from cartapp.models import Cart

from mainpage.views import TemplateClass


class CartView(TemplateClass):
    template_name = 'cart.html'
    title = 'корзина'


def add_view(request, pk):
    """
    Добавления товара в корзину
    :param request:
    :param pk:
    :return:
    """
    cart_uuid = request.COOKIES.get('cart_uuid')

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

    return redirect(request.META.get('HTTP_REFERER'))


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
