from django.db import models

from cinema.models.cinema import CinemaHall
from cinema.models.movie import Movie
from cinema.models.user import User


class Session(models.Model):
    cinema_hall = models.ForeignKey(CinemaHall, related_name='sessions', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='sessions', on_delete=models.CASCADE)
    session_date = models.DateTimeField()


class Ticket(models.Model):
    session = models.ForeignKey(Session, related_name='tickets', on_delete=models.CASCADE)
    ticket_price = models.IntegerField()
    status = models.BooleanField()


class UserTicket(models.Model):
    user = models.ForeignKey(User, related_name='tickets', on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, related_name='tickets', on_delete=models.CASCADE)
