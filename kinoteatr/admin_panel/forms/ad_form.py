from django import forms
from django_summernote.fields import SummernoteWidget

from cinema.models.page import Ad
from cinema.models.gallery import AdsGallery


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        exclude = ('seo',)
        widgets = {
            'title': forms.TextInput(attrs={'id': 'adName', 'class': 'form-control'}),
            'description': SummernoteWidget(attrs={'summernote': {'width': '100%'}}),
            'main_image': forms.FileInput(attrs={'id': 'main_image', 'class': 'upload'}),
            'url': forms.URLInput(attrs={'id': 'url', 'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'id': 'status', 'class': 'custom-control-input',
                                                 'type': 'checkbox'}),
            'publication_date': forms.DateInput(format='%Y-%m-%d', attrs={'id': 'adPublicationDate',
                                                                          'type': 'date',
                                                                          'class': 'form-control'})
        }


class AdGalleryForm(forms.ModelForm):
    class Meta:
        model = AdsGallery
        fields = ('image', )
        widgets = {
            'image': forms.FileInput(attrs={'id': 'gallery_image', 'class': 'upload'})
        }


AdGalleryFormSet = forms.inlineformset_factory(Ad, AdsGallery,
                                                 form=AdGalleryForm, max_num=4, extra=4, can_delete=False)
