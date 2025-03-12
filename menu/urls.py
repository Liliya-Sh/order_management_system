"""
URL конфигурация для приложения menu.
"""
from django.urls import path

from .views import MenuListView, ProductDetailView

app_name = 'menu'


urlpatterns = [
    path('', MenuListView.as_view(), name='menu'),
    path('product/<slug:product_slug>/', ProductDetailView.as_view(), name='product_detail'),

]
