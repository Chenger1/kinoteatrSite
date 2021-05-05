from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from cinema.models.page import Ad, News

from cinema.services.get_banners import get_context_for_generic_views

import datetime


class ListInstanceMixin(ListView):
    model = None
    template_name = None
    paginate_by = 12

    def get_queryset(self):
        queryset = self.model.objects.filter(status=True, publication_date__lte=datetime.date.today())
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context.update(get_context_for_generic_views())
        if self.model.__name__ == 'Ad':
            context['ad'] = True
        elif self.model.__name__ == 'News':
            context['news'] = True
        else:
            context['undefined'] = True
        return context


class InstanceDetailMixin(DetailView):
    model = None
    template_name = None
    context_object_name = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context_for_generic_views())
        if self.model.__name__ == 'Ad':
            context['ad'] = True
        elif self.model.__name__ == 'News':
            context['news'] = True
        else:
            context['undefined'] = True
        return context


class ListAd(ListInstanceMixin):
    model = Ad
    template_name = 'pages/list_cards.html'


class ListNews(ListInstanceMixin):
    model = News
    template_name = 'pages/list_cards.html'


class AdDetail(InstanceDetailMixin):
    model = Ad
    template_name = 'pages/detail_card.html'


class NewsDetail(InstanceDetailMixin):
    model = News
    template_name = 'pages/detail_card.html'
