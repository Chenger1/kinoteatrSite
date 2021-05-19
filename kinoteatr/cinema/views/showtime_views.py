from django.views.generic import View
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from cinema.services.get_banners import get_context_for_generic_views
from cinema.models.cinema import Cinema
from cinema.models.session import Session
from cinema.models.movie import Movie

import json
import datetime


class ShowTime(View):
    template_name = 'showtime.html'

    def get(self, request, pk=None):
        context = get_context_for_generic_views()
        if pk:
            cinema = get_object_or_404(Cinema, pk=pk)
            context['cinemas'] = list(Cinema.objects.exclude(pk=pk))
            context['cinemas'].append(cinema)
            context['cinemas'] = context['cinemas'][::-1]
        else:
            context['cinemas'] = Cinema.objects.all()

        return render(request, self.template_name, context)


class ShowTimeSession(View):
    def get(self, request):
        cinema = get_object_or_404(Cinema, pk=request.GET.get('selected_cinema'))

        if request.GET.get('selected_period') == '1':
            day = period = datetime.date.today() + datetime.timedelta(days=1)
        else:
            day = datetime.date.today()
            period = day + datetime.timedelta(days=int(request.GET.get('selected_period')))
        formats = json.loads(request.GET.get('selected_formats'))
        if formats:
            sessions = Session.objects.filter(cinema_hall__cinema=cinema,
                                              session_datetime_start__date__range=[day, period],
                                              type__in=[int(movie_format) for movie_format in formats])
        else:
            sessions = Session.objects.filter(cinema_hall__cinema=cinema,
                                              session_datetime_start__date__range=[day, period])
        if request.GET.get('selected_movie') and request.GET.get('selected_movie') != 'null':
            sessions = sessions.filter(movie__pk=request.GET.get('selected_movie'))

        context = self.get_context(sessions.order_by('session_datetime_start'))
        context['cinema'] = cinema.name
        context.update({'select_movies':
                        list(Movie.objects.values('name', 'pk').filter(sessions__cinema_hall__cinema=cinema,
                                                                       sessions__session_datetime_start__date__range=[day, period]).distinct())})

        return JsonResponse(context)

    def get_context(self, sessions):
        context = {}
        for index, session in enumerate(sessions):
            context.update({f'{index}': {
                'cinema': session.cinema_hall.cinema.name,
                'movie': session.movie.name,
                'movie_url': session.movie.get_absolute_public_url(),
                'image_url': session.movie.main_image.url,
                'session_date': session.session_datetime_start.strftime('%d %b'),
                'start_time': session.session_datetime_start.strftime('%H:%m'),
                'session_url': session.get_absolute_public_url(),
                'format': session.get_type_display(),
                'age_limit': session.movie.age_limit
            }})

        return context
