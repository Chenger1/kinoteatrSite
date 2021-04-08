from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.db import transaction

from cinema.models.movie import Movie

from admin_panel.forms.movie_form import MovieForm, MovieGalleryFormSet
from admin_panel.forms.seo_form import SeoForm


class ListMovies(View):
    template_name = 'movie/list_movies.html'

    def get(self, request):
        movies = Movie.objects.all()
        return render(request, self.template_name, {'movies': movies})


class AddMovie(CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movie/movie_detail.html'
    context_object_name = 'form'
    success_url = reverse_lazy('admin_panel:list_movie_admin')

    def get_context_data(self, **kwargs):
        data = super(AddMovie, self).get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = MovieGalleryFormSet(self.request.POST, self.request.FILES)
            data['seo_form'] = SeoForm(self.request.POST)
        else:
            data['formset'] = MovieGalleryFormSet()
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
                return super(AddMovie, self).form_invalid(form)
            if seo_form.is_valid():
                self.object.seo = seo_form.save()
            else:
                return super(AddMovie, self).form_invalid(form)
        return super(AddMovie, self).form_valid(form)
