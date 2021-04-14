from cinema.models.page import AboutCinema
from cinema.models.gallery import AboutCinemaGallery

from admin_panel.forms.about_cinema_form import AboutCinemaForm, AboutCinemaGalleryFormSet

from admin_panel.views.singleton_pages_mixin import EditSingletonMixin, DeleteSingletonGalleryImageMixin


class EditAboutCinema(EditSingletonMixin):
    model = AboutCinema
    template_name = 'about_cinema/edit_about_cinema.html'
    inline_form_set = AboutCinemaGalleryFormSet
    form_class = AboutCinemaForm


class DeleteAboutCinemaGalleryImage(DeleteSingletonGalleryImageMixin):
    model = AboutCinemaGallery
    redirect_url = 'admin_panel:edit_about_cinema_admin'
