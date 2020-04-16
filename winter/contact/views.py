"""
    Contact app
"""
from django.shortcuts import render

from cartapp.models import Cart


def index_view(request):
    """ Contact content
    :param request:
    :return:
    """

    """
    Получаем колличество товаров в корзине
    todo Вынести этот код в общий контроллер, чтобы не дублировать его в каждом приложении
    тема с контроллерами будет рассматриваться на последнем уроке.
    """
    cart = Cart.objects.filter(cart_uuid=request.COOKIES.get('cart_uuid')).all()

    content = {
        'title': 'контакты',
        'cart': cart
    }
    return render(request, 'contact.html', content)
