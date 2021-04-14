from cinema.models.page import Advertisement
from cinema.models.gallery import AdvertisementGallery

from admin_panel.forms.advertisement_form import AdvertisementForm, AdvertisementGalleryFormSet
from admin_panel.views.singleton_pages_mixin import EditSingletonMixin, DeleteSingletonGalleryImageMixin


class EditAdvertisement(EditSingletonMixin):
    model = Advertisement
    template_name = 'advertisement/edit_advertisement.html'
    inline_form_set = AdvertisementGalleryFormSet
    form_class = AdvertisementForm


class DeleteAdvertisementGalleryImage(DeleteSingletonGalleryImageMixin):
    model = AdvertisementGallery
    redirect_url = 'admin_panel:edit_advertisement_admin'
