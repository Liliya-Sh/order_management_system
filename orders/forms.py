from django import forms

from .models import Order


class OrderCreateForm(forms.ModelForm):
    """Форма для создания заказа."""
    class Meta:
        model = Order
        fields = ['table_number']


class SearchForm(forms.Form):
    """Форма для поиска заказа по id или статусу"""
    id = forms.IntegerField(label="ID",
                            required=False,
                            widget=forms.TextInput(attrs={'class': 'form-input'}))

    STATUS_CHOICES = [
        ('', 'Выберите статус'),
        (Order.PENDING, 'В ожидании'),  # Используйте константы из модели
        (Order.PAID, 'Оплачено'),
        (Order.READY, 'Готово'),
    ]

    status = forms.ChoiceField(label='Статус', choices=STATUS_CHOICES, required=False,
                               widget=forms.Select(attrs={'class': 'form-input'}))


class UpdateStatusForm(forms.ModelForm):
    """Форма для изменения статуса заказа"""

    STATUS_CHOICES = [
        (Order.PENDING, 'В ожидании'),  # Используйте константы из модели
        (Order.PAID, 'Оплачено'),
        (Order.READY, 'Готово'),
    ]

    status = forms.ChoiceField(label='', choices=STATUS_CHOICES, required=False,
                               widget=forms.Select(attrs={'class': 'form-input'}))

    class Meta:
        model = Order
        fields = ['status']


class DeleteForm(forms.Form):
    """Форма для удаления заказа по id"""
    id = forms.IntegerField(label="ID",
                            required=False,
                            widget=forms.TextInput(attrs={'class': 'form-input'}))
