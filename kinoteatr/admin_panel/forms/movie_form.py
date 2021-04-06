from django import forms

from cinema.models.movie import Movie, ExtendedInfo
from cinema.models.gallery import MovieGallery


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('name', 'description', 'main_image', 'url',
                  'is_2d', 'is_3d', 'is_imax', 'status', 'release')


class ExtendedInfoForm(forms.ModelForm):
    class Meta:
        model = ExtendedInfo
        fields = ('language', 'director', 'running_time', 'country', 'genre', 'age_limit')


class MovieGalleryInlineForm(forms.ModelForm):
    class Meta:
        model = MovieGallery
        fields = ('image',)


movie_gallery_form_set = forms.inlineformset_factory(Movie, MovieGallery,
                                                     form=MovieGalleryInlineForm, max_num=5, extra=5)
