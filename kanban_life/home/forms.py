from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(
        label='Senha',
        required=True,
    )

    class Meta:
        model = User

        exclude = [
            'id', 'last_login', 'date_joined'
        ]