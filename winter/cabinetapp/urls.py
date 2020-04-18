from django.urls import path

from . import views
from .views import WishlistView

app_name = 'cabinetapp'

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('wish-list/', WishlistView.as_view(), name='wishlist'),
    path('wish-list/add/<int:pk>', views.wishlist_add, name='wishlist_add'),
    path('wish-list/delete/<int:pk>', views.wishlist_add, name='wishlist_delete'),
]