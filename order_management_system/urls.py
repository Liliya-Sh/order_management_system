from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from menu.views import page_not_found


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('menu/', include('menu.urls', namespace='menu')),
    path('', include('users.urls', namespace='users')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found
