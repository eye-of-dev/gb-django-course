from django.urls import path

from . import views

app_name = 'cartapp'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('checkout/', views.checkout_view, name='checkout'),
]