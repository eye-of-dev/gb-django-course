"""winter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the includes() function: from django.urls import includes, path
    2. Add a URL to urlpatterns:  path('blog/', includes('blog.urls'))
"""
from django.urls import path, include
from . import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', include('mainpage.urls', namespace='mainpage')),
    path('admin/', include('adminapp.urls', namespace='admin')),
    path('auth/', include('authapp.urls', namespace='authapp')),
    path('cabinet/', include('cabinetapp.urls', namespace='cabinetapp')),
    path('cart/', include('cartapp.urls', namespace='cartapp')),
    path('checkout/', include('checkoutapp.urls', namespace='checkoutapp')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('shop/', include('shop.urls', namespace='shop')),

    path('', include('social_django.urls', namespace='social'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
