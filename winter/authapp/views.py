from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect

from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm

from django.views.generic import CreateView


class LoginClass(LoginView):
    form_class = ShopUserLoginForm
    authentication_form = ShopUserLoginForm
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_next(self):
        return self.request.GET['next'] if 'next' in self.request.GET.keys() else ''

    def get_context_data(self, **kwargs):
        context = super(LoginClass, self).get_context_data(**kwargs)
        context['title'] = 'авторизация'
        context['next'] = self.get_next()
        return context


class RegistrationClass(CreateView):
    pass


class LogoutClass(LogoutView):
    template_name = None
    next_page = 'mainpage:index'


def registration_view(request):
    """
    Регистрация на сайте
    :param request:
    :return:
    """
    if request.user.is_authenticated:
        return redirect('mainpage:index')

    register_form = ShopUserRegisterForm(request.POST, request.FILES)
    if request.method == 'POST' and register_form.is_valid():
        register_form.save()
        return redirect('authapp:login')

    content = {
        'title': 'регистрация',
        'register_form': register_form
    }
    return render(request, 'registration.html', content)
