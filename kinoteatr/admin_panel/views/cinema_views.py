from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.db import transaction

from admin_panel.forms.cinema_forms import CinemaForm, CinemaGalleryFormSet, CinemaHallForm, CinemaHallGalleryFormSet
from admin_panel.forms.seo_form import SeoForm
from cinema.models.cinema import Cinema, CinemaHall
from cinema.models.gallery import CinemaGallery, CinemaHallGallery

from admin_panel.views.page_views_mixin import AddPageMixin, UpdatePageMixin, DeleteMixin, DeleteGalleryImageMixin
from admin_panel.views.permission_mixin import AdminPermissionMixin


class ListCinema(AdminPermissionMixin, View):
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


class DeleteCinema(DeleteMixin):
    model = Cinema
    redirect_url = 'admin_panel:list_cinema_admin'


class DeleteCinemaGalleryImage(DeleteGalleryImageMixin):
    model = CinemaGallery
    redirect_url = 'admin_panel:edit_cinema_admin'


class AddCinemaHall(AdminPermissionMixin, CreateView):
    model = CinemaHall
    form_class = CinemaHallForm
    inline_form_set = CinemaHallGalleryFormSet
    template_name = 'cinema/edit_cinema_hall.html'
    success_url = reverse_lazy('admin_panel:list_cinema_admin')

    def get(self, request, *args, **kwargs):
        self.cinema = self.get_cinema(kwargs.get('pk'))
        return super(AddCinemaHall, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = self.inline_form_set(self.request.POST, self.request.FILES)
            data['seo_form'] = SeoForm(self.request.POST)
            data['cinema'] = self.get_cinema(self.request.POST.get('cinema_id'))
        else:
            data['formset'] = self.inline_form_set()
            data['seo_form'] = SeoForm()
            data['cinema'] = self.cinema
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        seo_form = context['seo_form']
        self.cinema = self.get_cinema(self.request.POST.get('cinema_id'))
        self.object = form.save(commit=False)
        self.object.cinema = self.cinema
        self.object.save()
        with transaction.atomic():
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
            else:
                return super().form_invalid(form)
            if seo_form.is_valid():
                self.object.seo = seo_form.save()
            else:
                return super().form_invalid(form)
        self.success_url = reverse_lazy('admin_panel:edit_cinema_admin', args=[self.cinema.pk])
        return super().form_valid(form)

    def get_cinema(self, pk):
        return get_object_or_404(Cinema, pk=pk)


class UpdateCinemaHall(UpdatePageMixin):
    model = CinemaHall
    form_class = CinemaHallForm
    inline_form_set = CinemaHallGalleryFormSet
    template_name = 'cinema/edit_cinema_hall.html'

    def get_context_data(self, **kwargs):
        self.success_url = reverse_lazy('admin_panel:edit_cinema_admin', args=[self.object.cinema.pk])
        return super().get_context_data(**kwargs)


class DeleteCinemaHall(AdminPermissionMixin, View):
    model = CinemaHall

    def get(self, request, pk):
        inst = get_object_or_404(self.model, pk=pk)
        seo = inst.seo
        cinema = inst.cinema.pk
        seo.delete()
        inst.delete()
        return redirect('admin_panel:edit_cinema_admin', pk=cinema)


class DeleteCinemaHallGalleryImage(DeleteGalleryImageMixin):
    model = CinemaHallGallery
    redirect_url = 'admin_panel:edit_cinema_hall'
