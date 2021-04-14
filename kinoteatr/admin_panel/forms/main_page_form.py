from django import forms

from cinema.models.page import MainPage


class MainPageForm(forms.ModelForm):
    class Meta:
        model = MainPage
        exclude = ('seo', )
        widgets = {
            'phone_number1': forms.TextInput(attrs={'id': 'phoneNumber1', 'class': 'form-control'}),
            'phone_number2': forms.TextInput(attrs={'id': 'phoneNumber2', 'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'id': 'status', 'class': 'custom-control-input',
                                                 'type': 'checkbox'}),
        }
