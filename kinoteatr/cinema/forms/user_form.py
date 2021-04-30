from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError


User = get_user_model()


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id': 'email', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password', 'class': 'form-control'}))

    errors_messages = {
        'inactive': 'Этот аккаунт уже не активен',
        'invalid_login': 'Введите правильный email и пароль',
    }

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.user_cache = authenticate(self.request, username=email, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError(
                self.errors_messages['inactive']
            )

    def get_user(self):
        return self.user_cache

    def get_invalid_login_error(self):
        return ValidationError(
            self.errors_messages['invalid_login'])