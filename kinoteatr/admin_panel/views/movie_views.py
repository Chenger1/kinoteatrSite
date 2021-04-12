from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.db import transaction

from cinema.models.movie import Movie
from cinema.models.gallery import MovieGallery

from admin_panel.forms.movie_form import MovieForm, MovieGalleryFormSet
from admin_panel.forms.seo_form import SeoForm

from admin_panel.views.page_views_mixin import AddPageMixin


class ListMovies(View):
    template_name = 'movie/list_movies.html'

    def get(self, request):
        movies = Movie.objects.all()
        released = movies.filter(released=True)
        soon = movies.filter(released=False)
        return render(request, self.template_name, {'released_movies': released,
                                                    'movies_soon': soon})


class AddMovie(AddPageMixin):
    model = Movie
    form_class = MovieForm
    inline_form_set = MovieGalleryFormSet
    template_name = 'movie/edit_movie.html'
    success_url = reverse_lazy('admin_panel:list_movie_admin')


class UpdateMovie(UpdateView):
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('admin_panel:list_movie_admin')
    context_object_name = 'form'
    template_name = 'movie/edit_movie.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateMovie, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = MovieGalleryFormSet(self.request.POST,
                                                     self.request.FILES,
                                                     instance=self.object)
            context['formset'].full_clean()
            context['seo_form'] = SeoForm(self.request.POST,
                                          instance=self.object.seo)
        else:
            context['formset'] = MovieGalleryFormSet(instance=self.object)
            context['seo_form'] = SeoForm(instance=self.object.seo)
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset = context['formset']
        seo_form = context['seo_form']
        response = super().form_valid(form)
        with transaction.atomic():
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
            else:
                return super(UpdateMovie, self).form_invalid(form)
            if seo_form.is_valid():
                self.object.seo = seo_form.save()
            else:
                return super(UpdateMovie, self).form_invalid(form)
        return response


class DeleteMovie(View):
    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        seo = movie.seo
        seo.delete()
        movie.delete()
        return redirect('admin_panel:list_movie_admin')


class DeleteMovieGalleryImage(View):
    model = MovieGallery

    def get(self, request, pk):
        inst = get_object_or_404(self.model, pk=pk)
        movie_pk = inst.entity.pk
        inst.delete()
        return redirect('admin_panel:edit_movie_admin', pk=movie_pk)


class DetailMovie(DetailView):
    model = Movie
    template_name = 'movie/movie_detail.html'
    context_object_name = 'movie'
