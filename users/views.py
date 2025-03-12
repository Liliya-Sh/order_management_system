"""
Модуль представлений для приложения users_employee.
"""
from django.contrib.auth.views import LoginView


from .forms import LoginUserEmployeeForm


# pylint: disable=R0901
class LoginUser(LoginView):
    """Авторизация сотрудников"""
    forms_class = LoginUserEmployeeForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}
