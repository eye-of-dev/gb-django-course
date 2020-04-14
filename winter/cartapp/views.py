from django.shortcuts import render


def index_view(request):
    """ Корзина
    :param request:
    :return:
    """
    content = {
        'title': 'корзина',
        'cart': []
    }
    return render(request, 'cart.html', content)


def checkout_view(request):
    pass
