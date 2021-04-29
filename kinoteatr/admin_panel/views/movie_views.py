from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.detail import DetailView

from cinema.models.movie import Movie
from cinema.models.gallery import MovieGallery

from admin_panel.forms.movie_form import MovieForm, MovieGalleryFormSet

from admin_panel.views.page_views_mixin import AddPageMixin, UpdatePageMixin, DeleteMixin, DeleteGalleryImageMixin
from admin_panel.views.permission_mixin import AdminPermissionMixin

import datetime


class ListMovies(AdminPermissionMixin, View):
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

    def get_context_data(self, **kwargs):
        """
        Set to context each session for given movie for the next 7 days
        """
        context = super().get_context_data(**kwargs)
        today = datetime.date.today()
        week = today + datetime.timedelta(days=7)  # get last day of the current 7-days period
        upcoming_session = self.object.sessions.filter(session_datetime_start__range=[today, week])
        # filter by date range
        context['sessions'] = upcoming_session
        return context
