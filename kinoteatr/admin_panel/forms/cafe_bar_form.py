from django import forms
from django_summernote.fields import SummernoteWidget

from cinema.models.page import CafeBar
from cinema.models.gallery import CafeBarGallery


class CafeBarForm(forms.ModelForm):
    class Meta:
        model = CafeBar
        exclude = ('seo',)
        widgets = {
            'title': forms.TextInput(attrs={'id': 'cafeBarName', 'class': 'form-control'}),
            'description': SummernoteWidget(attrs={'summernote': {'width': '100%'}}),
            'main_image': forms.FileInput(attrs={'id': 'main_image', 'class': 'upload'}),
            'status': forms.CheckboxInput(attrs={'id': 'status', 'class': 'custom-control-input',
                                                 'type': 'checkbox'}),
        }


class CafeBarGalleryForm(forms.ModelForm):
    class Meta:
        model = CafeBarGallery
        fields = ('image', )
        widgets = {
            'image': forms.FileInput(attrs={'id': 'gallery_image', 'class': 'upload'})
        }


CafeBarGalleryFormSet = forms.inlineformset_factory(CafeBar, CafeBarGallery,
                                                    form=CafeBarGalleryForm, max_num=4, extra=4,
                                                    can_delete=False)
