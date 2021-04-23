from django import forms
from django_summernote.fields import SummernoteWidget

from cinema.models.page import MobileApp
from cinema.models.gallery import MobileAppGallery


class MobileAppForm(forms.ModelForm):
    class Meta:
        model = MobileApp
        exclude = ('seo',)
        widgets = {
            'title': forms.TextInput(attrs={'id': 'mobileAppName', 'class': 'form-control'}),
            'description': SummernoteWidget(attrs={'summernote': {'width': '100%'}}),
            'main_image': forms.FileInput(attrs={'id': 'main_image', 'class': 'upload'}),
            'status': forms.CheckboxInput(attrs={'id': 'status', 'class': 'custom-control-input',
                                                 'type': 'checkbox'}),
        }


class MobileAppGalleryForm(forms.ModelForm):
    class Meta:
        model = MobileAppGallery
        fields = ('image', )
        widgets = {
            'image': forms.FileInput(attrs={'id': 'gallery_image', 'class': 'upload'})
        }


MobileAppGalleryFormSet = forms.inlineformset_factory(MobileApp, MobileAppGallery,
                                                      form=MobileAppGalleryForm, max_num=4, extra=4,
                                                      can_delete=False)
