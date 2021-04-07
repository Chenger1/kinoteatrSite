from django.shortcuts import render, redirect
from django.views.generic import View

from cinema.models.movie import Movie

from admin_panel.forms.movie_form import MovieForm, movie_gallery_form_set
from admin_panel.forms.seo_form import SeoForm
from admin_panel.utils.messages import beautify_error_messages


class ListMovies(View):
    template_name = 'movie/list_movies.html'

    def get(self, request):
        movies = Movie.objects.all()
        return render(request, self.template_name, {'movies': movies})


class AddMovie(View):
    movie_form = MovieForm
    movie_gallery_form = movie_gallery_form_set

    template_name = 'movie/movie_detail.html'

    def get(self, request):
        movie_form = self.movie_form()
        movie_gallery_inline_form = self.movie_gallery_form(prefix='movie')

        return render(request, self.template_name, {'movie_form': movie_form,
                                                    'movie_gallery_form': movie_gallery_inline_form})

    def post(self, request):
        movie_form = self.movie_form(request.POST, request.FILES)
        seo_form = SeoForm(request.POST)
        movie_gallery_inline_form = movie_gallery_form_set(request.POST, request.FILES, prefix='movie')
        context = {'movie_form': movie_form,
                   'seo_form': seo_form,
                   'movie_gallery_form': movie_gallery_inline_form,
                   'errors': []}

        if movie_form.is_valid():
            movie = movie_form.save()
            movie_gallery_inline_form = movie_gallery_form_set(request.POST, request.FILES, instance=movie,
                                                               prefix='movie')
            if movie_gallery_inline_form.is_valid():
                movie_gallery_inline_form.save()
            else:
                context['errors'] = 'Error with gallery image'
            if seo_form.is_valid():
                seo = seo_form.save()
                movie.seo_id = seo
                movie.save()
            else:
                context['errors'] = beautify_error_messages(seo_form.errors)
        else:
            context['errors'] = beautify_error_messages(movie_form.errors)

        if context['errors']:
            return render(request, self.template_name, context)
        else:
            return redirect('admin_panel:list_movie_admin')
