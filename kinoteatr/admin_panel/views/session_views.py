from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic import View
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http import JsonResponse

from cinema.models.session import Session, Ticket
from cinema.models.cinema import Cinema, CinemaHall
from cinema.models.movie import Movie

from admin_panel.views.permission_mixin import AdminPermissionMixin
from admin_panel.forms.session_form import AddSessionForm
from admin_panel.services.adding_session import Saver

import datetime
import json


class DisplaySessions(AdminPermissionMixin, View):
    model = Session
    template_name = 'sessions/list_session.html'

    def get(self, request):
        date_string = request.GET.get('date')  # need to filter by date
        if date_string:
            self.date = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
        else:  # if date_string is None -> filter by current date
            self.date = datetime.datetime.now().date()

        object_list = self.model.objects.filter(session_datetime_start__date=self.date)  # filter by session start time
        cinema = request.GET.get('cinema')
        if cinema:  # filtering by cinema
            object_list = object_list.filter(cinema_hall__cinema=cinema)
            cinema = int(cinema)  # cinema pk has to be transformed to integer, otherwise it can`t be seen in template
# if the way i need

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
            if not self.request.POST.get('end_session'):  # if not end session time - creates only one instance
                self.object = super().form_valid(form)
                return self.object
            else:  # if end session time has been given - created multiple instances for each day until the last
                obj = form.save(commit=False)
                saver = Saver(self.form_class, obj, context, self.request.POST)
                result: [AddSessionForm] = saver.save_multiple()
                # Saver class proceed multiple days and create form for each one
                if result:
                    for obj_form in result:  # save each form
                        obj_form.save()
                    return super().form_valid(form)
                return super().form_invalid(form)
        return super().form_invalid(form)


class DetailSession(AdminPermissionMixin, DetailView):
    model = Session
    template_name = 'sessions/detail.html'
    context_object_name = 'session'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reserved_tickets'] = json.dumps(self.get_reserved_tickets())
        context['schema_json'] = json.dumps(self.object.session_hall_schema)
        return context

    def get_reserved_tickets(self) -> dict:
        """
            Get all tickets for the given session.
            Prepare dict(which will be transformed to json) with info that uses on client side
            'row_number_string' for find specific row
            'seat_number' element index if row children list
            'ticket_state': 0 - ticket is reserved. 1 - ticket is bought
            'ticket_pk': contains ticket pk to manage them
        """
        session_tickets = self.object.tickets.all()
        result = {}

        for ticket in session_tickets:
            row_number_string = f'row_{ticket.row_number}'  # row has id in format 'row_0'. Uses ticket row number
            # as unique identifier of each row
            result.setdefault(row_number_string, []).append({'seat_number': ticket.seat_number,
                                                             'ticket_state': ticket.ticket_state,
                                                             # 0 - ticket is reserved. 1 - is bought
                                                             'ticket_pk': ticket.pk})  # pk - for manage tickets
        return result


class RevertTicketReserving(AdminPermissionMixin, View):
    model = Ticket

    def get(self, request, pk):
        """
        Gets string with tickets pk in string format like '1,2,3,4,'
        All pk`s separates with comma.
        First of all, they need to be split in list of pk`s
        Then, iterates over all of pk`s, finds ticket and deletes it.
        Finally, redirects to session using pk argument
        """
        tickets: str = request.GET.get('tickets_to_revert')  # 'format '1,2,3,4'.

        for ticket in tickets.split(','):
            get_object_or_404(self.model, pk=ticket).delete()
        return redirect('admin_panel:detail_session_admin', pk=pk)


class CinemaHallFormat(View):
    def get(self, request):
        #  Check, which format cinema hall supports
        # AJAX
        cinema_hall = get_object_or_404(CinemaHall, pk=request.GET.get('cinema_hall'))
        context = {}
        if cinema_hall.is_2d:
            context['2D'] = '1'
        if cinema_hall.is_3d:
            context['3D'] = '2'
        if cinema_hall.is_imax:
            context['IMAX'] = '3'
        #  Client side uses this info for render select tag only with available formats
        return JsonResponse(context, status=200)
