from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.detail import DetailView

from cinema.models.movie import Movie
from cinema.models.gallery import MovieGallery

from admin_panel.forms.movie_form import MovieForm, MovieGalleryFormSet

from admin_panel.views.page_views_mixin import AddPageMixin, UpdatePageMixin, DeleteMixin, DeleteGalleryImageMixin


class ListMovies(View):
    template_name = 'movie/list_movies.html'

    def get(self, request):
        movies = Movie.objects.all()
        released = movies.filter(released=True)
        soon = movies.filter(released=False)
        return render(request, self.template_name, {'released_movies': released,
                                                    'movies_soon': soon})


class AddMovie(AddPageMixin):
    model = Movie
    form_class = MovieForm
    inline_form_set = MovieGalleryFormSet
    template_name = 'movie/edit_movie.html'
    success_url = reverse_lazy('admin_panel:list_movie_admin')


class UpdateMovie(UpdatePageMixin):
    model = Movie
    form_class = MovieForm
    inline_form_set = MovieGalleryFormSet
    template_name = 'movie/edit_movie.html'
    context_object_name = 'form'
    success_url = reverse_lazy('admin_panel:list_movie_admin')


class DeleteMovie(DeleteMixin):
    model = Movie
    redirect_url = 'admin_panel:list_movie_admin'


class DeleteMovieGalleryImage(DeleteGalleryImageMixin):
    model = MovieGallery
    redirect_url = 'admin_panel:edit_movie_admin'


class DetailMovie(DetailView):
    model = Movie
    template_name = 'movie/movie_detail.html'
    context_object_name = 'movie'
