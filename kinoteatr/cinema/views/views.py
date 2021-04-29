from django.shortcuts import render
from django.views.generic import View

from cinema.services.get_banners import get_singleton_inst, get_page
from cinema.services.utils import get_current_date
from cinema.models.banners import OnTopBanner, BackgroundImage, SliderBanner
from cinema.models.page import MainPage, Advertisement
from cinema.models.movie import Movie


class DisplayMainPage(View):
    template_name = 'cinema_index.html'
    pages = [OnTopBanner, BackgroundImage, MainPage, SliderBanner,
             Advertisement]

    def get(self, request):
        context = self.get_context()

        return render(request, self.template_name, context)

    def get_context(self):
        context = get_page(self.pages)

        context['released_movie'] = Movie.objects.filter(released=True)
        context['movie_soon'] = Movie.objects.filter(released=False)
        context['day'] = get_current_date()

        return context


class ListMovies(View):
    template_name = 'nav_pages/show_movies_list.html'
    pages = [OnTopBanner, BackgroundImage, MainPage, Advertisement]

    def get(self, request):
        context = self.get_context()
        return render(request, self.template_name, context)

    def get_context(self):
        context = get_page(self.pages)
        context['released_movie'] = Movie.objects.filter(released=True)
        context['movie_soon'] = Movie.objects.filter(released=False)
        return context
