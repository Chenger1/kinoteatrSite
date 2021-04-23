from cinema.models.page import MobileApp
from cinema.models.gallery import MobileAppGallery

from admin_panel.forms.mobile_app_form import MobileAppForm, MobileAppGalleryFormSet

from admin_panel.views.singleton_pages_mixin import EditSingletonMixin, DeleteSingletonGalleryImageMixin


class EditMobileApp(EditSingletonMixin):
    model = MobileApp
    template_name = 'mobile_app/edit_mobile_app.html'
    inline_form_set = MobileAppGalleryFormSet
    form_class = MobileAppForm


class DeleteMobileAppGalleryImage(DeleteSingletonGalleryImageMixin):
    model = MobileAppGallery
    redirect_url = 'admin_panel:edit_mobile_app_admin'
