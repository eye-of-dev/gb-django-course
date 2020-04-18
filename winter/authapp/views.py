from django.contrib import auth
from django.contrib.auth import logout
from django.shortcuts import render, redirect

from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm

from cartapp.models import Cart


def login_view(request):
    """
    Вход в личный кабинет
    :param request:
    :return:
    """
    login_form = ShopUserLoginForm(data=request.POST or None)

    next = request.GET['next'] if 'next' in request.GET.keys() else ''

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)

            """
            При авторазации проверяем делал ли заказы пользователь как гость. 
            Если есть, то прикрепляем эти заказы авторизованному пользователю.
            """
            Cart.objects.filter(cart_uuid=request.COOKIES.get('cart_uuid')).all().update(user=request.user)

            if 'next' in request.POST.keys():
                return redirect(request.POST['next'])

            return redirect('mainpage:index')

    content = {
        'title': 'авторизация',
        'login_form': login_form,
        'next': next
    }
    return render(request, 'login.html', content)


def registration_view(request):
    """
    Регистрация на сайте
    :param request:
    :return:
    """

    register_form = ShopUserRegisterForm(request.POST, request.FILES)
    if request.method == 'POST' and register_form.is_valid():
        register_form.save()
        return redirect('authapp:login')

    content = {
        'title': 'регистрация',
        'register_form': register_form
    }
    return render(request, 'registration.html', content)


def logout_view(request):
    logout(request)
    return redirect('mainpage:index')
