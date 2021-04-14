from cinema.models.page import CafeBar
from cinema.models.gallery import CafeBarGallery

from admin_panel.forms.cafe_bar_form import CafeBarForm, CafeBarGalleryFormSet
from admin_panel.views.singleton_pages_mixin import EditSingletonMixin, DeleteSingletonGalleryImageMixin


class EditCafeBar(EditSingletonMixin):
    model = CafeBar
    template_name = 'cafe_bar/edit_cafe_bar.html'
    inline_form_set = CafeBarGalleryFormSet
    form_class = CafeBarForm


class DeleteCafeBarGalleryImage(DeleteSingletonGalleryImageMixin):
    model = CafeBarGallery
    redirect_url = 'admin_panel:edit_cafe_bar_admin'
