"""
URL конфигурация для приложения users_employee.
"""
from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = "users"


urlpatterns = [
    path('', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
