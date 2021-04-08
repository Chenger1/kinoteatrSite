from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.edit import CreateView

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
        else:
            data['formset'] = MovieGalleryFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super(AddMovie, self).form_valid(form)
