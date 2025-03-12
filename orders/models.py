from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models
from django.urls import reverse

from menu.models import Menu


class Order(models.Model):
    """Заказ, который сделал клиент"""
    objects = None

    PENDING = 'В ожидании'
    PAID = 'Оплачено'
    READY = 'Готово'

    STATUS = [
        (PENDING, 'В ожидании'),
        (PAID, 'Оплачено'),
        (READY, 'Готово'),
    ]

    user = models.ForeignKey(get_user_model(),
                             on_delete=models.SET_NULL,
                             related_name='orders',
                             null=True,
                             blank=True)
    table_number = models.PositiveIntegerField(validators=[MaxValueValidator(20)],
                                               blank=True, verbose_name='Номер стола')
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    update_time = models.DateTimeField(auto_now=True, verbose_name='Дата изменения заказа')

    status = models.CharField(
        max_length=11,
        choices=STATUS,
        default=PENDING,
        verbose_name='Статус заказа')

    class Meta:
        ordering = ['pk']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ {self.id} для стола {self.table_number}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_absolute_url(self):
        return reverse('orders:order_detail',  args=[self.pk])


class OrderItem(models.Model):
    """Составляющие заказа"""
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Menu,
                                related_name='order_items',
                                on_delete=models.CASCADE,
                                verbose_name='Код блюда')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Сумма')
    discount = models.DecimalField(max_digits=6, decimal_places=2, default=0, verbose_name='Скидка в %')

    class Meta:
        ordering = ['pk']

    def get_cost(self):
        return round(self.price * self.quantity, 2)

    def __str__(self):
        return str(self.id)
