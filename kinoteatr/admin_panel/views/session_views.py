from django.views.generic.edit import CreateView
from django.views.generic import View
from django.shortcuts import render
from django.urls import reverse_lazy

from cinema.models.session import Session
from cinema.models.cinema import Cinema
from cinema.models.movie import Movie

from admin_panel.views.permission_mixin import AdminPermissionMixin
from admin_panel.forms.session_form import AddSessionForm
from admin_panel.services.adding_session import Saver

import datetime


class DisplaySessions(AdminPermissionMixin, View):
    model = Session
    template_name = 'sessions/list_session.html'

    def get(self, request):
        date_string = request.GET.get('date')
        if date_string:
            self.date = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
        else:
            self.date = datetime.datetime.now().date()

        object_list = self.model.objects.filter(session_datetime_start__date=self.date)
        cinema = request.GET.get('cinema')
        if cinema:
            object_list = object_list.filter(cinema_hall__cinema=cinema)
            cinema = int(cinema)

        return render(request, self.template_name, {'date': self.date, 'sessions': object_list,
                                                    'cinemas': Cinema.objects.all(),
                                                    'current_cinema': cinema})


class AddSession(AdminPermissionMixin, CreateView):
    model = Session
    form_class = AddSessionForm
    context_object_name = 'form'
    template_name = 'sessions/add_session.html'
    success_url = reverse_lazy('admin_panel:display_sessions_admin')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cinemas'] = Cinema.objects.all()
        context['movies'] = Movie.objects.all()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        if form.is_valid():
            if not self.request.POST.get('end_session'):
                self.object = super().form_valid(form)
                return self.object
            else:
                obj = form.save(commit=False)
                saver = Saver(self.form_class, obj, context, self.request.POST)
                result = saver.save_multiple()
                if result:
                    for obj_form in result:
                        obj_form.save()
                    return super().form_valid(form)
                return super().form_invalid(form)
        return super().form_invalid(form)
