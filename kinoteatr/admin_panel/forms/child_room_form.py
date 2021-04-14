from django import forms
from django_summernote.fields import SummernoteWidget

from cinema.models.page import ChildRoom
from cinema.models.gallery import ChildRoomGallery


class ChildRoomForm(forms.ModelForm):
    class Meta:
        model = ChildRoom
        exclude = ('seo',)
        widgets = {
            'title': forms.TextInput(attrs={'id': 'childRoomName', 'class': 'form-control'}),
            'description': SummernoteWidget(attrs={'summernote': {'width': '100%'}}),
            'main_image': forms.FileInput(attrs={'id': 'main_image', 'class': 'upload'}),
            'status': forms.CheckboxInput(attrs={'id': 'status', 'class': 'custom-control-input',
                                                 'type': 'checkbox'}),
        }


class ChildRoomGalleryForm(forms.ModelForm):
    class Meta:
        model = ChildRoomGallery
        fields = ('image', )
        widgets = {
            'image': forms.FileInput(attrs={'id': 'gallery_image', 'class': 'upload'})
        }


ChildRoomGalleryFormSet = forms.inlineformset_factory(ChildRoom, ChildRoomGallery,
                                                      form=ChildRoomGalleryForm, max_num=4, extra=4,
                                                      can_delete=False)
