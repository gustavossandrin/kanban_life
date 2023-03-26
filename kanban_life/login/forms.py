from django import forms
from django.contrib.auth import authenticate
from kanban_life.home.models import User


class LoginForm(forms.Form):
    email = forms.CharField(
        label='Email',
        max_length=1000,
    )

    password = forms.CharField(
        label='Senha:',
        max_length=1000,
        widget=forms.PasswordInput
    )

    def clean_username(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email):
            raise forms.ValidationError(u'Usuário não encontrado.')
        return email

    def clean_password(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if not authenticate(email=email, password=password):
            raise forms.ValidationError(u'Senha incorreta.')
        return password

    def save(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        return authenticate(email=email, password=password)