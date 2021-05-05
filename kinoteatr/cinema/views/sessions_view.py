from django.views.generic.detail import DetailView
from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from cinema.services.get_banners import get_context_for_generic_views
from cinema.models.session import Session
from cinema.models.banners import OnTopBanner, BackgroundImage
from cinema.models.page import MainPage, Advertisement, CafeBar
from cinema.models.cinema import CinemaHall

from cinema.forms.session_form import TicketForm

from cinema.services.session_utils import get_session_data

import json


class SessionDetail(DetailView):
    model = Session
    template_name = 'session/detail_session.html'
    context_object_name = 'session'
    pages = [OnTopBanner, BackgroundImage, MainPage, Advertisement, CafeBar]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        banners_context = get_context_for_generic_views(self.pages)
        context['BackgroundImage'] = banners_context['BackgroundImage']
        context['OnTopBanner'] = banners_context['OnTopBanner']
        context['MainPage'] = banners_context['MainPage']
        context['Advertisement'] = banners_context['Advertisement']
        return context


class GetHallSchema(View):
    def get(self, request):
        cinema_pk = request.GET.get('cinema_hall_pk')
        session = get_object_or_404(Session, pk=request.GET.get('session'))
        reserved_tickets = self.get_reserved_tickets(session)
        schema = json.loads(get_object_or_404(CinemaHall, pk=cinema_pk).schema_json)
        return JsonResponse({'schema': schema,
                             'reserved_tickets': reserved_tickets,
                             'ticket_price': session.ticket_price
                             })

    def get_reserved_tickets(self, session) -> dict:
        """
            Get all tickets for the given session.
            Prepare dict(which will be transformed to json) with info that uses on client side
            'row_number_string' for find specific row
            'seat_number' element index if row children list
            'ticket_state': 0 - ticket is reserved. 1 - ticket is bought
            'ticket_pk': contains ticket pk to manage them
        """
        session_tickets = session.tickets.all()
        result = {}

        for ticket in session_tickets:
            row_number_string = f'row_{ticket.row_number}'  # row has id in format 'row_0'. Uses ticket row number
            # as unique identifier of each row
            result.setdefault(row_number_string, []).append({'seat_number': ticket.seat_number,
                                                             'ticket_state': ticket.ticket_state,
                                                             # 0 - ticket is reserved. 1 - is bought
                                                             'ticket_pk': ticket.pk})  # pk - for manage tickets
        return result


class WorkWithTicket(View):
    reserve = False
    buy = False

    def get(self, request):
        info = json.loads(request.GET.get('tickets'))
        session = get_object_or_404(Session, pk=request.GET.get('session'))
        for key in info.keys():
            for seat_number in info[key]:
                data = {'session': session,
                        'row_number': int(key),
                        'seat_number': int(seat_number),
                        'reserved': self.reserve,
                        'bought': self.buy,
                        'user': request.user}
                form = TicketForm(data)
                if form.is_valid():
                    form.save()
        return JsonResponse(get_session_data(session.pk, request.GET.get('cinema_hall_pk')))


class ReserveTicket(WorkWithTicket):
    reserve = True


class BuyTicket(WorkWithTicket):
    buy = True
