from django.urls import reverse_lazy
from django.views.generic.list import ListView

from cinema.models.page import News
from cinema.models.gallery import NewsGallery

from admin_panel.views.page_views_mixin import AddPageMixin, UpdatePageMixin, DeleteMixin, DeleteGalleryImageMixin
from admin_panel.forms.news_form import NewsForm, NewsGalleryFormSet


class ListNews(ListView):
    template_name = 'news/list_news.html'
    model = News
    paginate_by = 10
    context_object_name = 'news'


class AddNews(AddPageMixin):
    model = News
    form_class = NewsForm
    inline_form_set = NewsGalleryFormSet
    template_name = 'news/edit_news.html'
    success_url = reverse_lazy('admin_panel:list_news_admin')


class UpdateNews(UpdatePageMixin):
    model = News
    form_class = NewsForm
    inline_form_set = NewsGalleryFormSet
    template_name = 'news/edit_news.html'
    success_url = reverse_lazy('admin_panel:list_news_admin')


class DeleteNews(DeleteMixin):
    model = News
    redirect_url = 'admin_panel:list_news_admin'


class DeleteNewsGalleryImage(DeleteGalleryImageMixin):
    model = NewsGallery
    redirect_url = 'admin_panel:edit_news_admin'
