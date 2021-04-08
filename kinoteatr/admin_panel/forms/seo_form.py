from django import forms

from cinema.models.seo import Seo


class SeoForm(forms.ModelForm):
    class Meta:
        model = Seo
        fields = '__all__'
        widgets = {
            'seo_title':  forms.TextInput(attrs={'id': 'seoTitle', 'class': 'form-control'}),
            'seo_url': forms.URLInput(attrs={'id': 'seoURL', 'class': 'form-control'}),
            'seo_keywords': forms.TextInput(attrs={'id': 'seoKeywords', 'class': 'form-control'}),
            'seo_description': forms.Textarea(attrs={'id': 'seoDescription', 'class': 'form-control'}),
        }
