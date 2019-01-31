from django import forms

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email


class RegistrationForm(forms.Form):
    username = forms.CharField(
        label='Логин', max_length=150, min_length=8, required=True,

        widget=forms.TextInput(),
    )
    email = forms.EmailField(
        label='Email', required=True,

        widget=forms.EmailInput(),
    )
    password = forms.CharField(
        label='Пароль', max_length=30, min_length=8, required=True,

        widget=forms.PasswordInput(),
    )

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     if User.objects.filter(username__iexact=username).exists():
    #         raise ValidationError(
    #             'Пользователь с таким именем уже есть.',
    #             code='invalid',
    #         )


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Логин', max_length=150, min_length=8, required=True,

        widget=forms.TextInput(),
    )
    password = forms.CharField(
        label='Пароль', max_length=30, min_length=8, required=True,

        widget=forms.PasswordInput(),
    )