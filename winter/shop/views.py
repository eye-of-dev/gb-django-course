"""
    Shop app
"""
from django.shortcuts import render


def index(request):
    """ Category content
    :param request:
    :return:
    """
    list_categories = [
        {'href': '#', 'title': 'Fruits and Vegetables'},
        {'href': '#', 'title': 'Electronics', 'sub_categories': [
            {'href': '#', 'title': 'Home Appliances'},
            {'href': '#', 'title': 'Smartphones'},
            {'href': '#', 'title': 'Kitchen Appliances'},
            {'href': '#', 'title': 'Computer Accessories'},
            {'href': '#', 'title': 'Meat Alternatives'},
        ]},
        {'href': '#', 'title': 'Cooking'},
        {'href': '#', 'title': 'Beverages'},
        {'href': '#', 'title': 'Home and Cleaning'}
    ]
    content = {
        'title': 'category',
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
