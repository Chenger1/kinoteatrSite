from django.shortcuts import render
from django.views.generic import View


class ListMovies(View):
    template_name = 'movie/list_movies.html'

    def get(self, request):
        return render(request, self.template_name)
