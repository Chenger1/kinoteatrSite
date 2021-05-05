from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from cinema.models.cinema import Cinema, CinemaHall
from cinema.models.session import Session

from cinema.services.get_banners import get_context_for_generic_views

import datetime
import json


class CinemaList(ListView):
    model = Cinema
    template_name = 'cinema/cinema_list.html'
    context_object_name = 'cinemas'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context_for_generic_views())

        return context


class CinemaDetail(DetailView):
    model = Cinema
    template_name = 'cinema/detail_cinema.html'
    context_object_name = 'cinema'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context_for_generic_views())
        context['sessions'] = Session.objects.filter(cinema_hall__cinema=self.object,
                                                     session_datetime_start__date=datetime.datetime.today())[:6]
        return context


class CinemaHallDetail(DetailView):
    model = CinemaHall
    template_name = 'cinema/detail_cinema_hall.html'
    context_object_name = 'cinema_hall'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context_for_generic_views())
        context['sessions'] = Session.objects.filter(cinema_hall=self.object,
                                                     session_datetime_start__date=datetime.datetime.today())[:6]
        return context


class GetCinemaHallSchema(View):
    model = CinemaHall

    def get(self, request):
        hall = get_object_or_404(self.model, pk=request.GET.get('cinema_hall_pk'))
        schema = json.loads(hall.schema_json)
        return JsonResponse({'schema': schema})
