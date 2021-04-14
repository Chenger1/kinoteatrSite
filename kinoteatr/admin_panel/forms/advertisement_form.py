from django import forms
from django_summernote.fields import SummernoteWidget

from cinema.models.page import Advertisement
from cinema.models.gallery import AdvertisementGallery


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        exclude = ('seo',)
        widgets = {
            'title': forms.TextInput(attrs={'id': 'advertisementName', 'class': 'form-control'}),
            'description': SummernoteWidget(attrs={'summernote': {'width': '100%'}}),
            'main_image': forms.FileInput(attrs={'id': 'main_image', 'class': 'upload'}),
            'status': forms.CheckboxInput(attrs={'id': 'status', 'class': 'custom-control-input',
                                                 'type': 'checkbox'}),
        }


class AdvertisementGalleryForm(forms.ModelForm):
    class Meta:
        model = AdvertisementGallery
        fields = ('image', )
        widgets = {
            'image': forms.FileInput(attrs={'id': 'gallery_image', 'class': 'upload'})
        }


AdvertisementGalleryFormSet = forms.inlineformset_factory(Advertisement, AdvertisementGallery,
                                                          form=AdvertisementGalleryForm, max_num=4, extra=4,
                                                          can_delete=False)
