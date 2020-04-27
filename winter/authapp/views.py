from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect

from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm
from django.urls import reverse_lazy

from django.views.generic import FormView


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


class RegistrationClass(FormView):
    form_class = ShopUserRegisterForm
    template_name = 'registration.html'
    success_url = reverse_lazy('authapp:login')

    def get_context_data(self, **kwargs):
        context = super(RegistrationClass, self).get_context_data(**kwargs)
        context['title'] = 'регистрация'
        return context

    def form_valid(self, form):
        register_form = self.form_class(self.request.POST, self.request.FILES)
        register_form.save()
        return redirect(self.success_url)


class LogoutClass(LogoutView):
    template_name = None
    next_page = 'mainpage:index'
