from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.http import JsonResponse

from cinema.services.get_banners import get_context_for_generic_views
from cinema.services.utils import get_current_date
from cinema.models.movie import Movie
from cinema.models.cinema import Cinema

import datetime


class DisplayMainPage(View):
    template_name = 'cinema_index.html'

    def get(self, request):
        context = self.get_context()

        return render(request, self.template_name, context)

    def get_context(self):
        context = {}
        context.update(get_context_for_generic_views())
        context['released_movie'] = Movie.objects.filter(released=True)
        context['movie_soon'] = Movie.objects.filter(released=False)
        context['day'] = get_current_date()

        return context


class ListMoviesMixin(View):
    template_name = 'movie/show_movies_list.html'
    current = None

    def get(self, request):
        context = self.get_context()
        return render(request, self.template_name, context)

    def get_context(self):
        context = {}
        context.update(get_context_for_generic_views())
        context['released_movie'] = Movie.objects.filter(released=True)
        context['movie_soon'] = Movie.objects.filter(released=False)
        if self.current == 'movies':
            context['current_movies'] = True
        elif self.current == 'soon':
            context['soon_movies'] = True
        else:
            context['undefined'] = True
        return context


class ListSoonMovies(ListMoviesMixin):
    current = 'soon'


class ListMovies(ListMoviesMixin):
    current = 'movies'


class MovieDetail(DetailView):
    model = Movie
    template_name = 'movie/movie_detail_public.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context_for_generic_views())

        today = datetime.date.today()
        week = today + datetime.timedelta(days=7)  # get last day of the current 7-days period

        sessions = self.object.sessions.filter(session_datetime_start__range=[today, week])
        context['cinemas'] = Cinema.objects.filter(halls__sessions__in=sessions).distinct()
        # set to context only cinemas when chosen movie has sessions

        return context


class MovieSessionDetail(View):
    def get(self, request):
        today = datetime.date.today()
        week = today + datetime.timedelta(days=7)  # get last day of the current 7-days period

        cinema = get_object_or_404(Cinema, pk=request.GET.get('cinema'))
        movie = get_object_or_404(Movie, pk=request.GET.get('movie'))
        sessions = movie.sessions.filter(cinema_hall__cinema=cinema, session_datetime_start__range=[today, week])
        if request.GET.get('format'):
            sessions = sessions.filter(type=int(request.GET.get('format')))

        return JsonResponse({'sessions': self.serialize_to_json(sessions)})

    def serialize_to_json(self, queryset):
        result = {}
        for index, inst in enumerate(queryset):
            result.update({f'{index}': {
                'cinema_hall': inst.cinema_hall.number,
                'cinema_hall_url': inst.cinema_hall.get_absolute_public_url(),
                'session_start': inst.session_datetime_start.strftime('%d %b, %H:%m'),
                'ticket_price': inst.ticket_price,
                'type': inst.get_type_display(),
                'detail': inst.get_absolute_public_url()
            }})
        return result
