from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='catalog'),
    path('product/', views.product, name='product')
]