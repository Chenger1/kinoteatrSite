from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import update_last_login


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


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password1'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password2'}))
    city = forms.CharField(required=False, widget=forms.TextInput(attrs={'id': 'city', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password1', 'password2', 'city')
        widgets = {
            'username': forms.TextInput(attrs={'id': 'username', 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'id': 'email', 'type': 'email', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'id': 'phoneNumber', 'class': 'form-control'})
        }

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 != password2:
            raise ValidationError('Введенные пароли не совпадают')
        else:
            validate_password(password2)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user


class EditInfoForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('is_staff', 'is_superuser', 'is_active', 'password', 'date_joined')

        widgets = {
            'phone_number': forms.TextInput(attrs={'id': 'phoneNumber', 'class': 'form-control disable'}),
            'first_name': forms.TextInput(attrs={'id': 'firstName', 'class': 'form-control disable'}),
            'last_name': forms.TextInput(attrs={'id': 'lastName', 'class': 'form-control disable'}),
            'address': forms.TextInput(attrs={'id': 'address', 'class': 'form-control disable'}),
            'card_number': forms.TextInput(attrs={'id': 'cardNumber', 'class': 'form-control disable'}),
            'city': forms.TextInput(attrs={'id': 'city', 'class': 'form-control disable'}),
            'language': forms.Select(attrs={'id': 'language', 'class': 'custom-select disable'}),
            'gender': forms.Select(attrs={'id': 'gender', 'class': 'custom-select disable'}),
            'birthday_date': forms.DateInput(format='%Y-%m-%d', attrs={'id': 'birthdayDate',
                                                                       'type': 'date',
                                                                       'class': 'form-control disable'}),
        }
    username = forms.CharField(required=False, widget=forms.TextInput(attrs={'id': 'username',
                                                                             'class': 'form-control disable'}))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'id': 'email',
                                                                            'class': 'form-control disable'}))

    def save(self, commit=True):
        user = super().save(commit=False)
        old_user = User.objects.get(pk=self.instance.pk)
        user.password = old_user.password
        user.username = old_user.username
        user.email = old_user.email
        if commit:
            user.save()
        update_last_login(None, user)
        return user
