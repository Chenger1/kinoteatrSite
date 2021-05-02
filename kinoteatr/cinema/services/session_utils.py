from django.shortcuts import get_object_or_404

from cinema.models.session import Session
from cinema.models.cinema import CinemaHall

import json


def get_session_data(session_pk, cinema_hall_pk) -> dict:
    session = get_object_or_404(Session, pk=session_pk)
    cinema_hall = get_object_or_404(CinemaHall, pk=cinema_hall_pk)
    reserved_tickets = get_reserved_tickets(session)
    schema = json.loads(cinema_hall.schema_json)
    return {'schema': schema,
            'reserved_tickets': reserved_tickets,
            'ticket_price': session.ticket_price}


def get_reserved_tickets(session) -> dict:
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
