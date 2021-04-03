from django.db import models

from cinema.models.seo import Seo
from cinema.models.user import User


def get_cinema_main_image_path(instance, filename):
    return f'cinema/{instance.name}/main_image/{filename}'


def get_cinema_logo_path(instance, filename):
    return f'cinema/{instance.name}/logo/{filename}'


def get_hall_main_image_path(instance, filename):
    return f'cinema_hall/{instance.number}/main_image/{filename}'


class Cinema(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    conditions = models.TextField(max_length=5000)
    on_top_banner = models.ImageField(upload_to=get_cinema_main_image_path)
    logo = models.ImageField(upload_to=get_cinema_logo_path)
    seo = models.ForeignKey(Seo, related_name='cinema', on_delete=models.CASCADE)


class CinemaHall(models.Model):
    cinema = models.ForeignKey(Cinema, related_name='halls', on_delete=models.CASCADE)
    number = models.IntegerField()
    description = models.TextField(max_length=5000)
    schema = models.ImageField(upload_to='cinema_hall/schema/')
    on_top_banner = models.ImageField(upload_to=get_hall_main_image_path)
    seo = models.ForeignKey(Seo, related_name='cinema_hall', on_delete=models.CASCADE)


class Ticket(models.Model):
    cinema_hall = models.ForeignKey(CinemaHall, related_name='tickets', on_delete=models.CASCADE)
    ticket_price = models.IntegerField()
    vip_ticket_price = models.IntegerField(blank=True)
    status = models.BooleanField()


class UserTicket(models.Model):
    user = models.ForeignKey(User, related_name='tickets', on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, related_name='user', on_delete=models.CASCADE)
