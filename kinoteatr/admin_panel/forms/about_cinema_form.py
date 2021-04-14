from django import forms
from django_summernote.fields import SummernoteWidget

from cinema.models.page import AboutCinema
from cinema.models.gallery import AboutCinemaGallery


class AboutCinemaForm(forms.ModelForm):
    class Meta:
        model = AboutCinema
        exclude = ('seo',)
        widgets = {
            'title': forms.TextInput(attrs={'id': 'aboutCinemaName', 'class': 'form-control'}),
            'description': SummernoteWidget(attrs={'summernote': {'width': '100%'}}),
            'main_image': forms.FileInput(attrs={'id': 'main_image', 'class': 'upload'}),
            'status': forms.CheckboxInput(attrs={'id': 'status', 'class': 'custom-control-input',
                                                 'type': 'checkbox'}),
        }


class AboutCinemaGalleryForm(forms.ModelForm):
    class Meta:
        model = AboutCinemaGallery
        fields = ('image', )
        widgets = {
            'image': forms.FileInput(attrs={'id': 'gallery_image', 'class': 'upload'})
        }


AboutCinemaGalleryFormSet = forms.inlineformset_factory(AboutCinema, AboutCinemaGallery,
                                                        form=AboutCinemaGalleryForm, max_num=4, extra=4,
                                                        can_delete=False)
