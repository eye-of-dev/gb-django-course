from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('category/<int:pk>', views.category_view, name='category_view'),
    path('product/', views.product, name='product')
]


