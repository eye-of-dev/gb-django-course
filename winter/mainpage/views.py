"""
    Mainpage app
"""
from django.shortcuts import render


def index(request):
    """ Mainpage content
    :param request:
    :return:
    """
    content = {
        'title': 'mainpage'
    }
    return render(request, 'index.html', content)
