from cinema.models.page import VipHall
from cinema.models.gallery import VipHallGallery

from admin_panel.forms.vip_hall_form import VipHallForm, VipHallGalleryFormSet
from admin_panel.views.singleton_pages_mixin import EditSingletonMixin, DeleteSingletonGalleryImageMixin


class EditVipHall(EditSingletonMixin):
    model = VipHall
    template_name = 'vip_hall/edit_vip_hall.html'
    inline_form_set = VipHallGalleryFormSet
    form_class = VipHallForm


class DeleteVipHallGalleryImage(DeleteSingletonGalleryImageMixin):
    model = VipHallGallery
    redirect_url = 'admin_panel:edit_vip_hall_admin'
