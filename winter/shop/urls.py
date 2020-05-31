from django.urls import path
from django.views.decorators.cache import cache_page

from .views import CatalogView, CategoryView, ProductView

app_name = 'shop'

urlpatterns = [
    path('', cache_page(3600)(CatalogView.as_view()), name='catalog'),
    path('category/<int:pk>', cache_page(3600)(CategoryView.as_view()), name='category_view'),
    path('product/<int:pk>', cache_page(3600)(ProductView.as_view()), name='product_view')
]


