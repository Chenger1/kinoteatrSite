from django.db import models

from cinema.models.cinema import CinemaHall
from cinema.models.movie import Movie
from cinema.models.user import User


class Session(models.Model):
    cinema_hall = models.ForeignKey(CinemaHall, related_name='sessions', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='sessions', on_delete=models.CASCADE)
    session_datetime_start = models.DateTimeField()
    session_datetime_end = models.DateTimeField()
    session_hall_schema = models.TextField()
    ticket_price = models.IntegerField()

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


class Ticket(models.Model):
    session = models.ForeignKey(Session, related_name='tickets', on_delete=models.CASCADE)
    row_number = models.IntegerField()
    seat_number = models.IntegerField()
    reserved = models.BooleanField(default=False)
    bought = models.BooleanField(default=False)

    @property
    def ticket_state(self):
        if self.bought:
            return 1
        elif self.reserved:
            return 0
        else:
            return None


class UserTicket(models.Model):
    user = models.ForeignKey(User, related_name='tickets', on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, related_name='tickets', on_delete=models.CASCADE)
