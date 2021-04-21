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

    @property
    def ticket_price(self):
        ticket = self.tickets.first()
        return ticket.ticket_price

    @property
    def tickets_count(self):
        return self.tickets.count()-1

    @property
    def income(self):
        return self.tickets_count*self.ticket_price


class Ticket(models.Model):
    session = models.ForeignKey(Session, related_name='tickets', on_delete=models.CASCADE)
    ticket_price = models.IntegerField()
    reserved = models.BooleanField(default=False)
    bought = models.BooleanField(default=False)


class UserTicket(models.Model):
    user = models.ForeignKey(User, related_name='tickets', on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, related_name='tickets', on_delete=models.CASCADE)
