from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserChangeForm

from cartapp.models import Cart


def login_view(request):
    """
    Вход в личный кабинет
    :param request:
    :return:
    """
    login_form = ShopUserLoginForm(data=request.POST or None)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)

            """
            todo При авторазации проверяем делал ли заказы пользователь как гость. 
            Если есть, то прикрепляем эти заказы авторизованному пользователю.
            Вынести этот функционал в общий контроллер. Тему будет проходить на последнем уроке.
            """
            Cart.objects.filter(cart_uuid=request.COOKIES.get('cart_uuid')).all().update(user=request.user)

            return redirect('mainpage:index')

    content = {
        'title': 'авторизация',
        'login_form': login_form
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


@login_required(login_url='authapp:login')
def profile_view(request):
    """
    Обновление личных данных(профиля) на сайте
    :param request:
    :return:
    """
    if request.method == 'POST':
        change_form = ShopUserChangeForm(request.POST, request.FILES, instance=request.user)
        if change_form.is_valid():
            change_form.save()
            return redirect('authapp:profile')
    else:
        change_form = ShopUserChangeForm(instance=request.user)

    content = {
        'title': 'редактирование профиля',
        'change_form': change_form
    }
    return render(request, 'profile.html', content)


def logout_view(request):
    logout(request)
    return redirect('mainpage:index')
