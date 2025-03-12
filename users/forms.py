"""
Формы для аутентификации и управления учетными записями сотрудников.
"""

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm


class LoginUserEmployeeForm(AuthenticationForm):
    """Форма для аутентификации сотрудников."""

    username = forms.CharField(label="Логин",
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Пароль",
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        """Метаданные для формы аутентификации."""
        model = get_user_model()
        fields = ['username', 'password']
