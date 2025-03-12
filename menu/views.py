from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound

from django.views.generic import ListView, DetailView

from cart.cart import Cart
from cart.forms import CartAddProductForm

from .models import *


class MenuListView(LoginRequiredMixin, ListView):
    """Главная страница пиццерии с Меню и корзиной"""
    model = Menu
    template_name = 'menu/menu.html'
    context_object_name = 'product'  # Имя переменной для списка продуктов

    def get_queryset(self):
        return Menu.available.all()  # Возвращаем только доступные продукты

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['category'] = Category.objects.all()
        context['cart_product_form'] = CartAddProductForm()
        context['cart'] = Cart(self.request)  # Создаем корзину
        return context


class ProductDetailView(LoginRequiredMixin, DetailView):
    """Просмотреть отдельный товар"""
    model = Menu
    template_name = 'menu/product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'  # Имя переменной для продукта

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        return context


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
