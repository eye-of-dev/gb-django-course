from django.conf.urls import url

from .views import LoginClass, LogoutClass, RegistrationClass, ConfirmClass

app_name = 'authapp'

urlpatterns = [
    url('login/', LoginClass.as_view(), name='login'),
    url('registration/', RegistrationClass.as_view(), name='registration'),
    url('confirm/', ConfirmClass.as_view(), name='confirm'),
    url(r'^confirm/(?P<activation_key>\w+)/$', ConfirmClass.as_view(), name='confirm_activation'),
    url('logout/', LogoutClass.as_view(), name='logout')
]
