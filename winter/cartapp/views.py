from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect

from django.template.loader import render_to_string
from shop.models import Products

from cartapp.models import Cart, CartCommon

from mainpage.views import TemplateClass


class CartView(TemplateClass):
    template_name = 'cart.html'
    title = 'корзина'


def add_action(request, pk):
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


def update_action(request, pk, quantity):
    """
    Обновляем колличество товара в корзине
    :param request:
    :param pk:
    :param quantity:
    :return:
    """
    if request.is_ajax():
        product = get_object_or_404(Cart, pk=pk)
        product.quantity = quantity
        product.save()

        cart = CartCommon(request.COOKIES.get('cart_uuid'))
        result = render_to_string('includes/cart_data.html', {'cart': cart})

        return JsonResponse({'result': result})


def delete_action(request, pk):
    """
    Удаление товаров из корзины
    :param request:
    :param pk:
    :return:
    """
    if request.is_ajax():
        product = get_object_or_404(Cart, pk=pk)
        product.delete()

        cart = CartCommon(request.COOKIES.get('cart_uuid'))
        result = render_to_string('includes/cart_data.html', {'cart': cart})

        return JsonResponse({'result': result})
