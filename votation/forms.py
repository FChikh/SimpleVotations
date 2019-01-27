from django import forms

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email


class RegistrationForm(forms.Form):
    username = forms.CharField(
        label='Логин', max_length=150, min_length=8, required=True,
        validators=[UnicodeUsernameValidator()],
        widget=forms.TextInput(),
    )
    email = forms.EmailField(
        label='Email', required=True,
        validators=[validate_email],
        widget=forms.EmailInput(),
    )
    password = forms.CharField(
        label='Пароль', max_length=30, min_length=8, required=True,
        validators=[validate_password],
        widget=forms.PasswordInput(),
    )


