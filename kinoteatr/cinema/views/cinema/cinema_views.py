from django.views.generic.list import ListView

from cinema.models.cinema import Cinema
from cinema.models.page import MainPage, Advertisement, AboutCinema
from cinema.models.banners import OnTopBanner, BackgroundImage

from cinema.services.get_banners import get_context_for_generic_views


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
