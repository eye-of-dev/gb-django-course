from django.urls import path

from .views import ProductsListView, ProductsCreateView, ProductsUpdateView, ProductsReadView, ProductsDeleteView, \
    UsersListView, UsersCreateView, UsersReadView, UsersUpdateView, UsersDeleteView, ProductsCategoriesListView, \
    ProductsCategoriesCreateView, ProductsCategoriesReadView, ProductsCategoriesUpdateView, \
    ProductsCategoriesDeleteView, OrdersListView, OrdersUpdateView, OrdersReadView, OrdersDeleteView

app_name = 'adminapp'

urlpatterns = [
    path('orders/index', OrdersListView.as_view(), name='orders_list'),
    # path('orderapp/create', OrdersCreateView.as_view(), name='orders_create'),
    path('orders/read/<int:pk>', OrdersReadView.as_view(), name='orders_read'),
    path('orders/update/<int:pk>', OrdersUpdateView.as_view(), name='orders_update'),
    path('orderapp/delete/<int:pk>', OrdersDeleteView.as_view(), name='orders_delete'),

    path('product-categories/index', ProductsCategoriesListView.as_view(), name='product_categories_index'),
    path('product-categories/create', ProductsCategoriesCreateView.as_view(), name='product_categories_create'),
    path('product-categories/read/<int:pk>', ProductsCategoriesReadView.as_view(), name='product_categories_read'),
    path('product-categories/update/<int:pk>', ProductsCategoriesUpdateView.as_view(), name='product_categories_update'),
    path('product-categories/delete/<int:pk>', ProductsCategoriesDeleteView.as_view(), name='product_categories_delete'),

    path('products/index', ProductsListView.as_view(), name='products_list'),
    path('products/create', ProductsCreateView.as_view(), name='products_create'),
    path('products/read/<int:pk>', ProductsReadView.as_view(), name='products_read'),
    path('products/update/<int:pk>', ProductsUpdateView.as_view(), name='products_update'),
    path('products/delete/<int:pk>', ProductsDeleteView.as_view(), name='products_delete'),

    path('users/index', UsersListView.as_view(), name='users_list'),
    path('users/create', UsersCreateView.as_view(), name='users_create'),
    path('users/read/<int:pk>', UsersReadView.as_view(), name='users_read'),
    path('users/update/<int:pk>', UsersUpdateView.as_view(), name='users_update'),
    path('users/delete/<int:pk>', UsersDeleteView.as_view(), name='users_delete')

]
