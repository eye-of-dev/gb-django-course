"""
    Contact app
"""
from django.shortcuts import render


def index_view(request):
    """ Contact content
    :param request:
    :return:
    """
    content = {
        'title': 'контакты'
    }
    return render(request, 'contact.html', content)
