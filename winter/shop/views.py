"""
    Shop app
"""
from django.shortcuts import render

from shop.models import ProductCategories

from shop.models import Products


def catalog(request):
    """ Category content
    :param request:
    :return:
    """
    list_categories = ProductCategories.objects.all()
    list_products = Products.objects.all()
    content = {
        'title': 'каталог',
        'list_categories': list_categories,
        'list_products': list_products
    }
    return render(request, 'category.html', content)


def category_view(request, pk):
    pass


def product(request):
    """ Product content
    :param request:
    :return:
    """
    content = {
        'title': 'продукт'
    }
    return render(request, 'product.html', content)
