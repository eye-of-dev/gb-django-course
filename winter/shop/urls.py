from django.urls import path

from .views import CatalogView, CategoryView, ProductView

app_name = 'shop'

urlpatterns = [
    path('', CatalogView.as_view(), name='catalog'),
    path('category/<int:pk>', CategoryView.as_view(), name='category_view'),
    path('product/<int:pk>', ProductView.as_view(), name='product_view')
]


