"""
    Mainpage app
"""
from django.shortcuts import render


def index_view(request):
    """ Mainpage content
    :param request:
    :return:
    """
    content = {
        'title': 'главная'
    }
    return render(request, 'index.html', content)
