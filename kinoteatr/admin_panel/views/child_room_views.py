from cinema.models.page import ChildRoom
from cinema.models.gallery import ChildRoomGallery

from admin_panel.forms.child_room_form import ChildRoomForm, ChildRoomGalleryFormSet

from admin_panel.views.singleton_pages_mixin import EditSingletonMixin, DeleteSingletonGalleryImageMixin


class EditChildRoom(EditSingletonMixin):
    model = ChildRoom
    template_name = 'child_room/edit_child_room.html'
    inline_form_set = ChildRoomGalleryFormSet
    form_class = ChildRoomForm


class DeleteChildRoomGalleryImage(DeleteSingletonGalleryImageMixin):
    model = ChildRoomGallery
    redirect_url = 'admin_panel:edit_child_room_admin'
