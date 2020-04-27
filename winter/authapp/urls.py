from django.urls import path

from . import views
from .views import LoginClass, LogoutClass

app_name = 'authapp'

urlpatterns = [
    path('login/', LoginClass.as_view(), name='login'),
    path('registration/', views.registration_view, name='registration'),
    path('logout/', LogoutClass.as_view(), name='logout')
]