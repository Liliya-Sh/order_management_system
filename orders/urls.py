from django.urls import path

from orders.views import OrderCreateView, OrderListView, OrderDetailView, OrderDelete, Revenue, OrderSearchView

app_name = 'orders'

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('order_list/', OrderListView.as_view(), name='order_list'),
    path('search/', OrderSearchView.as_view(), name='search'),
    path('order_detail/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('delete/<int:pk>/', OrderDelete.as_view(), name='delete'),
    path('revenue/', Revenue.as_view(), name='revenue'),
]
