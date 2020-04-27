from django.urls import path

from .views import LoginClass, LogoutClass, RegistrationClass

app_name = 'authapp'

urlpatterns = [
    path('login/', LoginClass.as_view(), name='login'),
    path('registration/', RegistrationClass.as_view(), name='registration'),
    path('logout/', LogoutClass.as_view(), name='logout')
]