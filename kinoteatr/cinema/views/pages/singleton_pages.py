from django.views.generic import View
from django.shortcuts import render

from cinema.models.banners import OnTopBanner, BackgroundImage
from cinema.models.page import MainPage, Advertisement, AboutCinema

from cinema.services.get_banners import get_context_for_generic_views


class DisplaySingletonPage(View):
    model = None
    template_name = None
    pages = [OnTopBanner, BackgroundImage, MainPage, Advertisement, AboutCinema]

    def get(self, request):
        context = {}
        instance = self.model.load()
        context.update(get_context_for_generic_views(self.pages))
        context['object'] = instance
        return render(request, self.template_name, context)


class DisplayAdvertisement(DisplaySingletonPage):
    model = Advertisement
    template_name = 'pages/advertisement.html'
