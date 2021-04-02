from django.shortcuts import render
from django.views.generic import View


class ListNews(View):
    # TODO - replace with ListView when News model will be added
    template_name = 'news/list_news.html'

    def get(self, request):
        return render(request, self.template_name)
