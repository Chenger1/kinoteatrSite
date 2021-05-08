from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from cinema.models.cinema import CinemaHall
from cinema.models.movie import Movie

User = get_user_model()


class Session(models.Model):
    types_choice = [
        (1, '2D'),
        (2, '3D'),
        (3, 'IMAX')
    ]

    cinema_hall = models.ForeignKey(CinemaHall, related_name='sessions', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='sessions', on_delete=models.CASCADE)
    session_datetime_start = models.DateTimeField()
    session_datetime_end = models.DateTimeField()
    session_hall_schema = models.TextField()
    ticket_price = models.IntegerField()
    type = models.IntegerField(choices=types_choice)

    @property
    def tickets_count(self):
        return self.tickets.filter(bought=True).count()

    @property
    def income(self):
        return self.tickets_count*self.ticket_price

    @property
    def available_seats(self):
        return self.cinema_hall.seats_amount - self.tickets_count

    @property
    def reserved_tickets(self):
        return self.tickets.filter(reserved=True).count()

    def get_absolute_public_url(self):
        return reverse('cinema:session_detail', args=[self.pk])


class Ticket(models.Model):
    session = models.ForeignKey(Session, related_name='tickets', on_delete=models.CASCADE)
    row_number = models.IntegerField()
    seat_number = models.IntegerField()
    reserved = models.BooleanField(default=False)
    bought = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name='tickets', on_delete=models.CASCADE, blank=True, null=True)

    @property
    def beauty_row_number(self):
        return self.row_number + 1

    @property
    def beauty_seat_number(self):
        return self.seat_number + 1

    @property
    def status(self):
        return 'Забронирован' if self.reserved else 'Куплен'

    @property
    def ticket_state(self):
        if self.bought:
            return 1
        elif self.reserved:
            return 0
        else:
            return None
