from django.views.generic import View
from django.shortcuts import render

from cinema.models.page import Advertisement, CafeBar, MobileApp, VipHall

from cinema.services.get_banners import get_context_for_generic_views


class DisplaySingletonPage(View):
    model = None
    template_name = 'pages/singleton_page.html'

    def get(self, request):
        context = {}
        instance = self.model.load()
        context.update(get_context_for_generic_views())
        context['object'] = instance
        return render(request, self.template_name, context)


class DisplayAdvertisement(DisplaySingletonPage):
    model = Advertisement


class DisplayCafeBar(DisplaySingletonPage):
    model = CafeBar


class DisplayMobileApp(DisplaySingletonPage):
    model = MobileApp


class DisplayVipHall(DisplaySingletonPage):
    model = VipHall
