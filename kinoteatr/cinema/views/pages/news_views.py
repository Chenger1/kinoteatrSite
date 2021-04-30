from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from cinema.models.page import News, Advertisement, MainPage, AboutCinema
from cinema.models.banners import OnTopBanner, BackgroundImage

from cinema.services.get_banners import get_context_for_generic_views

import datetime


class ListNews(ListView):
    model = News
    template_name = 'news/list_news_public.html'
    context_object_name = 'news'
    paginate_by = 12
    pages = [OnTopBanner, BackgroundImage, MainPage, Advertisement, AboutCinema]

    def get_queryset(self):
        queryset = self.model.objects.filter(status=True, publication_date__lte=datetime.date.today())
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context.update(get_context_for_generic_views(self.pages))

        return context


class NewsDetail(DetailView):
    model = News
    template_name = 'news/public_news_detail.html'
    context_object_name = 'news'
    pages = [OnTopBanner, BackgroundImage, MainPage, Advertisement, AboutCinema]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context_for_generic_views(self.pages))
        return context
