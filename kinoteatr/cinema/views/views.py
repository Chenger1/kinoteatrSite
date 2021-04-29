from django.shortcuts import render
from django.views.generic import View

from cinema.services.get_banners import get_singleton_inst
from cinema.services.utils import get_current_date
from cinema.models.banners import OnTopBanner, BackgroundImage, SliderBanner
from cinema.models.page import MainPage, Advertisement
from cinema.models.movie import Movie

import datetime


class DisplayMainPage(View):
    template_name = 'cinema_index.html'
    pages = [OnTopBanner, BackgroundImage, MainPage, SliderBanner,
             Advertisement]

    def get(self, request):
        context = self.get_context()

        return render(request, self.template_name, context)

    def get_context(self):
        context = {}
        for page in self.pages:
            context[page.__name__] = get_singleton_inst(page)

        context['released_movie'] = Movie.objects.filter(released=True)
        context['movie_soon'] = Movie.objects.filter(released=False)
        context['day'] = get_current_date()

        return context
