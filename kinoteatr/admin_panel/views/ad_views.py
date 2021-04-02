from django.shortcuts import render
from django.views.generic import View


class ListAds(View):
    # TODO - Rewrite using ListView
    template_name = 'ads/list_ads.html'

    def get(self, request):
        return render(request, self.template_name)
