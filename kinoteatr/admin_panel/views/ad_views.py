from django.urls import reverse_lazy
from django.views.generic.list import ListView

from cinema.models.page import Ad
from cinema.models.gallery import AdsGallery

from admin_panel.views.page_views_mixin import AddPageMixin, UpdatePageMixin, DeleteMixin, DeleteGalleryImageMixin
from admin_panel.forms.ad_form import AdForm, AdGalleryFormSet


class ListAds(ListView):
    template_name = 'ads/list_ads.html'
    model = Ad
    paginate_by = 10
    context_object_name = 'ads'


class AddAd(AddPageMixin):
    model = Ad
    form_class = AdForm
    inline_form_set = AdGalleryFormSet
    template_name = 'ads/edit_ad.html'
    success_url = reverse_lazy('admin_panel:list_ads_admin')


class UpdateAd(UpdatePageMixin):
    model = Ad
    form_class = AdForm
    inline_form_set = AdGalleryFormSet
    template_name = 'ads/edit_ad.html'
    success_url = reverse_lazy('admin_panel:list_ads_admin')


class DeleteAd(DeleteMixin):
    model = Ad
    redirect_url = 'admin_panel:list_ads_admin'


class DeleteAdGalleryImage(DeleteGalleryImageMixin):
    model = AdsGallery
    redirect_url = 'admin_panel:edit_ad_admin'
