from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from cinema.models.cinema import Cinema
from cinema.models.page import MainPage, Advertisement, AboutCinema
from cinema.models.banners import OnTopBanner, BackgroundImage
from cinema.models.session import Session

from cinema.services.get_banners import get_context_for_generic_views

import datetime


class CinemaList(ListView):
    model = Cinema
    template_name = 'cinema/cinema_list.html'
    context_object_name = 'cinemas'
    pages = [OnTopBanner, BackgroundImage, MainPage, Advertisement, AboutCinema]
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context_for_generic_views(self.pages))

        return context


class CinemaDetail(DetailView):
    model = Cinema
    template_name = 'cinema/detail_cinema.html'
    context_object_name = 'cinema'
    pages = [OnTopBanner, BackgroundImage, MainPage, Advertisement, AboutCinema]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context_for_generic_views(self.pages))
        context['sessions'] = Session.objects.filter(cinema_hall__cinema=self.object,
                                                     session_datetime_start__date=datetime.datetime.today())[:6]
        return context
