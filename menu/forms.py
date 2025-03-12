from django import forms

from .models import Messages


class MessagesForm(forms.ModelForm):
    """Форма для отправления сообщения пиццерии"""

    class Meta:
        model = Messages
        fields = ['sender_name', 'phone', 'email', 'message']
        widget = {
            'sender_name': forms.TextInput(attrs={'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'class': 'form-input',
                                            'pattern': '[0-9]*',
                                            'title': 'Пожалуйста, введите только цифры'}),
            'email': forms.TextInput(attrs={'class': 'form-input'}),
            'message': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }
