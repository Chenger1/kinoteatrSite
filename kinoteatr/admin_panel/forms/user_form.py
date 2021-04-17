from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import update_last_login


User = get_user_model()


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

        widgets = {
            'username': forms.TextInput(attrs={'id': 'username', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'id': 'email', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'id': 'phoneNumber', 'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'id': 'firstName', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'id': 'lastName', 'class': 'form-control'}),
            'address': forms.TextInput(attrs={'id': 'address', 'class': 'form-control'}),
            'card_number': forms.TextInput(attrs={'id': 'cardNumber', 'class': 'form-control'}),
            'city': forms.TextInput(attrs={'id': 'city', 'class': 'form-control'}),
            'language': forms.Select(attrs={'id': 'language', 'class': 'custom-select'}),
            'gender': forms.Select(attrs={'id': 'gender', 'class': 'custom-select'}),
            'birthday_date': forms.DateInput(format='%Y-%m-%d', attrs={'id': 'birthdayDate',
                                                                       'type': 'date',
                                                                       'class': 'form-control'}),
            'is_staff': forms.CheckboxInput(attrs={'id': 'isStaff', 'class': 'form-check-input',
                                                   'type': 'checkbox'}),
            'is_superuser': forms.CheckboxInput(attrs={'id': 'isSuperuser', 'class': 'form-check-input',
                                                       'type': 'checkbox'}),
            'is_active': forms.CheckboxInput(attrs={'id': 'isActive', 'class': 'form-check-input',
                                                    'type': 'checkbox'}),
        }

    date_joined = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d', attrs={'id': 'newsPublicationDate',
                                                                                   'type': 'date',
                                                                                   'class': 'form-control',
                                                                                   'disabled': 'true'}),
                                  required=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password', 'class': 'form-control'}),
                               required=False)

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data['password']
        if password:
            user.set_password(password)
        else:
            old_pass = User.objects.get(pk=self.instance.pk).password
            user.password = old_pass
        if commit:
            user.save()
        update_last_login(None, user)
        return user
