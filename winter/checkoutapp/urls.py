from django.urls import path

from .views import CheckoutClass, CheckoutSuccessClass

app_name = 'checkoutapp'

urlpatterns = [
    path('', CheckoutClass.as_view(), name='checkout'),
    path('success/', CheckoutSuccessClass.as_view(), name='success'),
]