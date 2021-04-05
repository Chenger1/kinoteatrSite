from django import forms

from cinema.models.banners import BackgroundImage


class BackgroundImageForm(forms.ModelForm):
    class Meta:
        model = BackgroundImage
        fields = ('image', 'status')
