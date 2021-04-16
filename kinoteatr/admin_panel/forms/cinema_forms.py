from django import forms
from django_summernote.fields import SummernoteWidget

from cinema.models.cinema import Cinema, CinemaHall
from cinema.models.gallery import CinemaGallery, CinemaHallGallery
from cinema.models.page import Contact


class CinemaForm(forms.ModelForm):
    class Meta:
        model = Cinema
        fields = ('name', 'description', 'conditions', 'on_top_banner',
                  'logo')
        widgets = {
            'name': forms.TextInput(attrs={'id': 'cinemaName', 'class': 'form-control'}),
            'description': SummernoteWidget(attrs={'summernote': {'width': '100%'}}),
            'conditions': SummernoteWidget(attrs={'summernote': {'width': '100%'}}),
            'on_top_banner': forms.FileInput(attrs={'id': 'on_top_banner', 'class': 'upload'}),
            'logo': forms.FileInput(attrs={'id': 'logo', 'class': 'upload'})
        }

    def save(self, commit=True):
        cinema_inst = super().save(commit=commit)
        if not hasattr(cinema_inst, 'contacts') and commit:
            Contact.objects.create(cinema=cinema_inst)
        return cinema_inst


class CinemaHallForm(forms.ModelForm):
    class Meta:
        model = CinemaHall
        fields = ('number', 'description',
                  'schema', 'on_top_banner')
        widgets = {
            'number': forms.NumberInput(attrs={'id': 'hallNumber', 'class': 'form-control'}),
            'description': SummernoteWidget(attrs={'summernote': {'width': '100%'}}),
            'on_top_banner': forms.FileInput(attrs={'id': 'on_top_banner', 'class': 'upload'}),
            'schema': forms.FileInput(attrs={'id': 'schema', 'class': 'upload'})
        }


class CinemaGalleryForm(forms.ModelForm):
    class Meta:
        model = CinemaGallery
        fields = ('image', )
        widgets = {
            'image': forms.FileInput(attrs={'id': 'cinema_image', 'class': 'upload'})
        }


class CinemaHallGalleryForm(forms.ModelForm):
    class Meta:
        model = CinemaHallGallery
        fields = ('image', )
        widgets = {
            'image': forms.FileInput(attrs={'id': 'cinema_hall_image', 'class': 'upload'})
        }


CinemaGalleryFormSet = forms.inlineformset_factory(Cinema, CinemaGallery,
                                                   form=CinemaGalleryForm, max_num=4, extra=4, can_delete=False)

CinemaHallGalleryFormSet = forms.inlineformset_factory(CinemaHall, CinemaHallGallery,
                                                       form=CinemaHallGalleryForm, max_num=4, extra=4, can_delete=False)
