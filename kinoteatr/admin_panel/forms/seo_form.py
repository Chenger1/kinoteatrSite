from django import forms

from cinema.models.seo import Seo


class SeoForm(forms.ModelForm):
    class Meta:
        model = Seo
        fields = '__all__'
