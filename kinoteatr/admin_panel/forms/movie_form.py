from django import forms

from cinema.models.movie import Movie
from cinema.models.gallery import MovieGallery


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('name', 'description', 'main_image', 'url',
                  'is_2d', 'is_3d', 'is_imax', 'status', 'release',
                  'language', 'director', 'running_time', 'country',
                  'genre', 'age_limit')

    release = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d',
                                                     attrs={'placeholder': '2000-01-01'}))

    running_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M',
                                                          attrs={'placeholder': '1:30'}))


class MovieGalleryInlineForm(forms.ModelForm):
    class Meta:
        model = MovieGallery
        fields = ('image',)


movie_gallery_form_set = forms.inlineformset_factory(Movie, MovieGallery,
                                                     form=MovieGalleryInlineForm, max_num=4, extra=4)
