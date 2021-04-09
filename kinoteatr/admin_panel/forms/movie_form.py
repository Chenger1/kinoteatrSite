from django import forms
from django_summernote.fields import SummernoteWidget

from cinema.models.movie import Movie
from cinema.models.gallery import MovieGallery


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('name', 'description', 'main_image', 'url',
                  'is_2d', 'is_3d', 'is_imax', 'release',
                  'language', 'director', 'running_time', 'country',
                  'genre', 'age_limit', 'released')
        widgets = {
            'name': forms.TextInput(attrs={'id': 'movieName', 'class': 'form-control'}),
            'description': SummernoteWidget(attrs={'summernote': {'width': '100%'}}),
            'main_image': forms.FileInput(attrs={'id': 'main_image', 'class': 'upload'}),
            'url': forms.URLInput(attrs={'id': 'url', 'class': 'form-control'}),
            'is_2d': forms.CheckboxInput(attrs={'id': '2DType', 'class': 'form-check-input type_checkbox',
                                                'type': 'checkbox', 'checked': 'true'}),
            'is_3d': forms.CheckboxInput(attrs={'id': '3DType', 'class': 'form-check-input type_checkbox',
                                                'type': 'checkbox', 'checked': 'true'}),
            'is_imax': forms.CheckboxInput(attrs={'id': 'imaxType', 'class': 'form-check-input type_checkbox',
                                                  'type': 'checkbox', 'checked': 'true'}),
            'release': forms.DateInput(format='%Y-%m-%d',
                                       attrs={'placeholder': '2000-01-01', 'id': 'release',
                                              'class': 'form-control'}),
            'running_time': forms.TimeInput(format='%H:%M',
                                            attrs={'placeholder': '1:30', 'id': 'running_time',
                                                   'class': 'form-control'}),
            'director': forms.TextInput(attrs={'id': 'movieDirector', 'class': 'form-control'}),
            'country': forms.TextInput(attrs={'id': 'movieCountry', 'class': 'form-control'}),
            'language': forms.Select(attrs={'id': 'movieLanguage', 'class': 'form-control form-select'}),
            'genre': forms.Select(attrs={'id': 'movieGenre', 'class': 'form-control form-select'}),
            'age_limit': forms.Select(attrs={'id': 'movieAgeLimit', 'class': 'form-control form-select'}),
            'released': forms.CheckboxInput(attrs={'id': 'released', 'class': 'form-check-input type_checkbox',
                                                   'type': 'checkbox'})

        }


class MovieGalleryInlineForm(forms.ModelForm):
    class Meta:
        model = MovieGallery
        fields = ('image',)
        widgets = {
            'image': forms.FileInput(attrs={'id': 'gallery_image', 'class': 'upload',
                                            'onchange': 'readURL(this)'})
        }


MovieGalleryFormSet = forms.inlineformset_factory(Movie, MovieGallery,
                                                  form=MovieGalleryInlineForm, max_num=4, extra=4, can_delete=False)
