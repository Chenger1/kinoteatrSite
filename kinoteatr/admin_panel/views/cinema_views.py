from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.db import transaction

from admin_panel.forms.cinema_forms import CinemaForm, CinemaGalleryFormSet
from admin_panel.forms.seo_form import SeoForm
from cinema.models.cinema import Cinema


class ListCinema(View):
    template_name = 'cinema/list_cinema.html'

    def get(self, request):
        cinemas = Cinema.objects.all()
        return render(request, self.template_name, {'cinemas': cinemas})


class AddCinema(CreateView):
    model = Cinema
    form_class = CinemaForm
    template_name = 'cinema/edit_cinema.html'
    context_object_name = 'form'
    success_url = reverse_lazy('admin_panel:list_cinema_admin')

    def get_context_data(self, **kwargs):
        data = super(AddCinema, self).get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = CinemaGalleryFormSet(self.request.POST, self.request.FILES)
            data['seo_form'] = SeoForm(self.request.POST)
        else:
            data['formset'] = CinemaGalleryFormSet()
            data['seo_form'] = SeoForm()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        seo_form = context['seo_form']
        self.object = form.save()
        with transaction.atomic():
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
            else:
                return super(AddCinema, self).form_invalid(form)
            if seo_form.is_valid():
                self.object.seo = seo_form.save()
            else:
                return super(AddCinema, self).form_invalid(form)
        return super(AddCinema, self).form_valid(form)
