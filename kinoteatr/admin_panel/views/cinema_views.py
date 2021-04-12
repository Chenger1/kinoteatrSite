from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View

from admin_panel.forms.cinema_forms import CinemaForm, CinemaGalleryFormSet
from cinema.models.cinema import Cinema

from admin_panel.views.page_views_mixin import AddPageMixin, UpdatePageMixin


class ListCinema(View):
    template_name = 'cinema/list_cinema.html'

    def get(self, request):
        cinemas = Cinema.objects.all()
        return render(request, self.template_name, {'cinemas': cinemas})


class AddCinema(AddPageMixin):
    model = Cinema
    form_class = CinemaForm
    inline_form_set = CinemaGalleryFormSet
    template_name = 'cinema/edit_cinema.html'
    context_object_name = 'form'
    success_url = reverse_lazy('admin_panel:list_cinema_admin')


class UpdateCinema(UpdatePageMixin):
    model = Cinema
    form_class = CinemaForm
    inline_form_set = CinemaGalleryFormSet
    template_name = 'cinema/edit_cinema.html'
    context_object_name = 'form'
    success_url = reverse_lazy('admin_panel:list_cinema_admin')
