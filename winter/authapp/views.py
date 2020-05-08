from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, get_object_or_404

from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm
from authapp.models import ShopUser

from django.urls import reverse_lazy

from django.views.generic import FormView

from mainpage.views import TemplateClass


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
    success_url = reverse_lazy('authapp:confirm')

    def get_context_data(self, **kwargs):
        context = super(RegistrationClass, self).get_context_data(**kwargs)
        context['title'] = 'регистрация'
        return context

    def form_valid(self, form):
        register_form = self.form_class(self.request.POST, self.request.FILES)
        user = register_form.save()
        user.send_verify_mail()
        return redirect(self.success_url)


class ConfirmClass(TemplateClass):
    template_name = 'confirm.html'
    title = 'подтверждение почты'
    authenticated = False

    def get_context_data(self, **kwargs):
        context = super(ConfirmClass, self).get_context_data(**kwargs)
        context['authenticated'] = self.authenticated
        return context

    def get(self, request, *args, **kwargs):
        context = super(ConfirmClass, self).get_context_data(**kwargs)
        if 'activation_key' in self.kwargs:
            user = get_object_or_404(ShopUser, is_active=False, activation_key=self.kwargs['activation_key'])
            if not user.is_activation_key_expired:
                user.is_active = True
                user.save()
                context['authenticated'] = True

        return self.render_to_response(context)


class LogoutClass(LogoutView):
    template_name = None
    next_page = 'mainpage:index'
