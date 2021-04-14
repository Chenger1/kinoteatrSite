from django import forms
from django_summernote.fields import SummernoteWidget

from cinema.models.page import VipHall
from cinema.models.gallery import VipHallGallery


class VipHallForm(forms.ModelForm):
    class Meta:
        model = VipHall
        exclude = ('seo',)
        widgets = {
            'title': forms.TextInput(attrs={'id': 'vipHallName', 'class': 'form-control'}),
            'description': SummernoteWidget(attrs={'summernote': {'width': '100%'}}),
            'main_image': forms.FileInput(attrs={'id': 'main_image', 'class': 'upload'}),
            'status': forms.CheckboxInput(attrs={'id': 'status', 'class': 'custom-control-input',
                                                 'type': 'checkbox'}),
        }


class VipHallGalleryForm(forms.ModelForm):
    class Meta:
        model = VipHallGallery
        fields = ('image', )
        widgets = {
            'image': forms.FileInput(attrs={'id': 'gallery_image', 'class': 'upload'})
        }


VipHallGalleryFormSet = forms.inlineformset_factory(VipHall, VipHallGallery,
                                                    form=VipHallGalleryForm, max_num=4, extra=4,
                                                    can_delete=False)
