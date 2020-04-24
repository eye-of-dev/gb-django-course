import adminapp.views as adminapp
from django.urls import path

from .views import ProductsListView, ProductsCreateView, ProductsUpdateView, ProductsReadView, ProductsDeleteView

app_name = 'adminapp'

urlpatterns = [
    path('product-categories/index', adminapp.product_categories_index, name='product_categories_index'),
    path('product-categories/create', adminapp.product_categories_create, name='product_categories_create'),
    path('product-categories/read/<int:pk>', adminapp.product_categories_read, name='product_categories_read'),
    path('product-categories/update/<int:pk>', adminapp.product_categories_update, name='product_categories_update'),
    path('product-categories/delete/<int:pk>', adminapp.product_categories_delete, name='product_categories_delete'),

    path('products/index', ProductsListView.as_view(), name='products_list'),
    path('products/create', ProductsCreateView.as_view(), name='products_create'),
    path('products/read/<int:pk>', ProductsReadView.as_view(), name='products_read'),
    path('products/update/<int:pk>', ProductsUpdateView.as_view(), name='products_update'),
    path('products/delete/<int:pk>', ProductsDeleteView.as_view(), name='products_delete')
]
