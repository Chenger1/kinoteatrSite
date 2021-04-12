from django.shortcuts import render
from django.views.generic import View

from admin_panel.forms.cinema_forms import CinemaForm
from cinema.models.cinema import Cinema


class ListCinema(View):
    template_name = 'cinema/list_cinema.html'

    def get(self, request):
        cinemas = Cinema.objects.all()
        return render(request, self.template_name, {'cinemas': cinemas})
