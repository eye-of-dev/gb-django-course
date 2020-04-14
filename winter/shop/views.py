"""
    Shop app
"""
from django.shortcuts import render, get_object_or_404

from shop.models import ProductCategories

from shop.models import Products


def catalog_view(request):
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
    category = get_object_or_404(ProductCategories, pk=pk)

    list_categories = ProductCategories.objects.all()
    list_products = Products.objects.filter(category=category.id).all()

    content = {
        'title': category.title,
        'category': category,
        'list_categories': list_categories,
        'list_products': list_products
    }

    return render(request, 'category.html', content)


def product_view(request):
    """ Product content
    :param request:
    :return:
    """
    content = {
        'title': 'продукт'
    }
    return render(request, 'product.html', content)
