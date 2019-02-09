from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(
        label='Логин', max_length=150, min_length=4, required=True,

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
        label='Логин', max_length=150, min_length=4, required=True,

        widget=forms.TextInput(),
    )
    password = forms.CharField(
        label='Пароль', max_length=50, min_length=8, required=True,

        widget=forms.PasswordInput(),
    )


class ProfileEditForm(forms.Form):
    username = forms.CharField(
        label='Логин', max_length=150, min_length=4, required=False,

        widget=forms.TextInput(),
    )
    email = forms.EmailField(
        label='Email', required=False,

        widget=forms.EmailInput(),
    )
    password = forms.CharField(
        label='Пароль', max_length=50, min_length=8, required=False,

        widget=forms.PasswordInput(),
    )


class VotingForm(forms.Form):
    vote = forms.CharField(
        max_length=1000, min_length=4, required=True,
    )


class Report(forms.Form):
    report = forms.CharField(
        max_length=1000, min_length=30, required=True,
    )
