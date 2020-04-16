"""
    Shop app
"""
from django.shortcuts import render, get_object_or_404

from shop.models import ProductCategories

from shop.models import Products

from cartapp.models import Cart


def catalog_view(request):
    """ Category content
    :param request:
    :return:
    """

    """
    Получаем колличество товаров в корзине
    todo Вынести этот код в общий контроллер, чтобы не дублировать его в каждом приложении
    тема с контроллерами будет рассматриваться на последнем уроке.
    """
    cart = Cart.objects.filter(cart_uuid=request.COOKIES.get('cart_uuid')).all()

    list_categories = ProductCategories.objects.all()
    list_products = Products.objects.all()
    content = {
        'title': 'каталог',
        'list_categories': list_categories,
        'list_products': list_products,
        'cart': cart
    }
    return render(request, 'category.html', content)


def category_view(request, pk):
    category = get_object_or_404(ProductCategories, pk=pk)

    """
    Получаем колличество товаров в корзине
    todo Вынести этот код в общий контроллер, чтобы не дублировать его в каждом приложении
    тема с контроллерами будет рассматриваться на последнем уроке.
    """
    cart = Cart.objects.filter(cart_uuid=request.COOKIES.get('cart_uuid')).all()

    list_categories = ProductCategories.objects.all()
    list_products = Products.objects.filter(category=category.id).all()

    content = {
        'title': category.title,
        'category': category,
        'list_categories': list_categories,
        'list_products': list_products,
        'cart': cart
    }

    return render(request, 'category.html', content)


def product_view(request, сpk, ppk):
    """ Product content
    :param request:
    :return:
    """
    category = get_object_or_404(ProductCategories, pk=сpk)
    product = get_object_or_404(Products, pk=ppk)

    similar_products = Products.objects.filter(category=category.id).exclude(pk=ppk).all()

    """
    Получаем колличество товаров в корзине
    todo Вынести этот код в общий контроллер, чтобы не дублировать его в каждом приложении
    тема с контроллерами будет рассматриваться на последнем уроке.
    """
    cart = Cart.objects.filter(cart_uuid=request.COOKIES.get('cart_uuid')).all()

    content = {
        'title': product.title,
        'category': category,
        'product': product,
        'similar_products': similar_products,
        'cart': cart
    }
    return render(request, 'product.html', content)
