from django.urls import path, include, re_path
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
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [re_path(r'^__debug__/', include(debug_toolbar.urls))]
