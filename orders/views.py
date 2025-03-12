from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View

from django.views.generic import CreateView, DetailView, FormView, DeleteView

from cart.cart import Cart

from cart.views import cart_detail
from .forms import OrderCreateForm, SearchForm, UpdateStatusForm
from .models import OrderItem, Order


class OrderCreateView(LoginRequiredMixin, CreateView):
    """Создание заказа"""
    form_class = OrderCreateForm
    template_name = 'orders/order/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = self.get_cart_details()
        return context

    def form_valid(self, form):
        cart = Cart(self.request)
        order = form.save(commit=False)

        if not self.is_valid_table_number(order.table_number):
            messages.error(self.request, "Номер стола должен быть положительным целым числом.")
            return self.form_invalid(form)  # Возвращаемся к форме с ошибкой

        if self.request.user.is_authenticated:
            order.user = self.request.user
        order.save()

        for item in cart:
            OrderItem.objects.create(order=order,
                                     product=item['product'],
                                     price=item['price'],
                                     quantity=item['quantity'])

        # Очистить корзину
        cart.clear()

        return render(self.request, 'orders/order/created.html', {'order': order})

    def is_valid_table_number(self, table_number):
        # Проверка, что номер стола является положительным целым числом
        return isinstance(table_number, int) and table_number > 0
    def get_cart_details(self):
        cart = Cart(self.request)
        return cart_detail(cart)


class OrderDetailView(LoginRequiredMixin, DetailView):
    """Просмотреть заказ по ID и изменить статус"""
    model = Order
    template_name = 'orders/order_detail.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orderitems'] = self.object.items.all()  # Получаем элементы только для текущего заказа
        context['status_form'] = UpdateStatusForm(instance=self.object)  # Передаем текущий статус в форму
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = UpdateStatusForm(request.POST, instance=self.object)
        if form.is_valid():
            form.save()  # Сохраняем изменения
            return redirect(self.get_success_url())
        return self.get(request, *args, **kwargs)
    def get_success_url(self):
        return reverse('orders:order_list')


class OrderListView(LoginRequiredMixin, FormView):
    """Представление для поиска заказов по ID или статусу"""
    form_class = SearchForm
    template_name = 'orders/order_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_orders'] = Order.objects.all()
        context['orderitems'] = OrderItem.objects.all()
        context['results'] = kwargs.get('results', [])
        return context

    def post(self, request, *args, **kwargs):
        order_id = request.POST.get('id')
        if order_id:
            try:
                order = Order.objects.get(id=order_id)
                order.delete()
                messages.success(request, "Заказ успешно удалён.")
            except Order.DoesNotExist:
                messages.error(request, "Заказ с таким ID не найден.")
        return redirect('orders:order_list')


class OrderSearchView(LoginRequiredMixin, FormView):
    """Представление для поиска заказов по ID или статусу"""
    form_class = SearchForm
    template_name = 'orders/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_form'] = UpdateStatusForm()
        context['orderitems'] = OrderItem.objects.all()
        context['results'] = kwargs.get('results', [])
        return context

    def form_valid(self, form):
        order_id = form.cleaned_data.get('id')
        status = form.cleaned_data.get('status')

        # Фильтрация заказов по ID и статусу
        results = Order.objects.all()
        if order_id:
            results = results.filter(id=order_id)
        if status:
            results = results.filter(status=status)

        if not results.exists():
            messages.warning(self.request, "Заказы не найдены по заданным критериям.")

        # Передаем результаты в контекст
        return self.render_to_response(self.get_context_data(form=form, results=results))


class OrderDelete(DeleteView):
    """Удаление заказа по ID"""
    model = Order
    template_name = 'orders/delete.html'  # Используйте отдельный шаблон для удаления
    context_object_name = 'order'
    success_url = reverse_lazy('orders:order_list')  # URL для перенаправления после удаления

    def post(self, request, *args, **kwargs):
        order_id = request.POST.get('id')
        if order_id:
            try:
                order = Order.objects.get(id=order_id)
                order.delete()
            except Order.DoesNotExist:
                # Обработка ошибки, например, перенаправление с сообщением
                messages.error(request, "Заказ не найден.")
        return redirect('orders:order_list')


class Revenue(LoginRequiredMixin, View):
    """Расчет выручки заказов со статусом Оплачен"""
    template_name = 'orders/revenue.html'

    def get(self, request, *args, **kwargs):
        paid_orders = Order.objects.filter(status=Order.PAID).prefetch_related('items')
        total_revenue = sum(order.get_total_cost() for order in paid_orders)

        context = {
            'orders': paid_orders,
            'total_revenue': total_revenue,
        }

        return render(request, self.template_name, context)
