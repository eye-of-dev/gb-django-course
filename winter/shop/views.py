"""
    Shop app
"""
from django.shortcuts import render

from shop.models import ProductCategories


def index(request):
    """ Category content
    :param request:
    :return:
    """
    list_categories = ProductCategories.objects.all()
    content = {
        'title': 'каталог',
        'list_categories': list_categories
    }
    return render(request, 'category.html', content)


def product(request):
    """ Product content
    :param request:
    :return:
    """
    content = {
        'title': 'product'
    }
    return render(request, 'product.html', content)
