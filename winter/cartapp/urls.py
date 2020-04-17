from django.urls import path

from . import views
from .views import CartView

app_name = 'cartapp'

urlpatterns = [
    path('', CartView.as_view(), name='index'),
    path('add/<int:pk>', views.add_view, name='add'),
    path('update/', views.update_view, name='update'),
    path('delete/', views.delete_view, name='delete'),
    path('checkout/', views.checkout_view, name='checkout'),
]