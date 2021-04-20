from django.db import models
from django.urls import reverse

from cinema.models.seo import Seo
from cinema.utils.get_valid_dir_name import get_valid_dir_name

import copy


def get_cinema_main_image_path(instance, filename):
    name = get_valid_dir_name(instance.name)
    return f'cinema/{name}/main_image/{filename}'


def get_cinema_logo_path(instance, filename):
    name = get_valid_dir_name(instance.name)
    return f'cinema/{name}/logo/{filename}'


def get_hall_main_image_path(instance, filename):
    return f'cinema_hall/{instance.number}/main_image/{filename}'


class Cinema(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=5000)
    conditions = models.TextField(max_length=5000)
    on_top_banner = models.ImageField(upload_to=get_cinema_main_image_path)
    logo = models.ImageField(upload_to=get_cinema_logo_path)
    seo = models.ForeignKey(Seo, related_name='cinema', on_delete=models.CASCADE,
                            blank=True, null=True)

    def get_images(self):
        return [self.on_top_banner.path, self.logo.path]

    def get_delete_url(self):
        return reverse('admin_panel:delete_cinema_admin', args=[self.pk])

    def __str__(self):
        return self.name


class CinemaHall(models.Model):
    cinema = models.ForeignKey(Cinema, related_name='halls', on_delete=models.CASCADE)
    number = models.IntegerField(unique=True)
    description = models.TextField(max_length=5000)
    schema = models.ImageField(upload_to='cinema_hall/schema/')
    schema_json = models.TextField(default='{}')
    on_top_banner = models.ImageField(upload_to=get_hall_main_image_path)
    seats_amount = models.IntegerField(default=0)
    seo = models.ForeignKey(Seo, related_name='cinema_hall', on_delete=models.CASCADE,
                            blank=True, null=True)

    creation_date = models.DateField(auto_now_add=True)

    def get_images(self):
        return [self.schema.path, self.on_top_banner.path]

    def clone_schema_json(self):
        return copy.deepcopy(self.schema_json)

    def get_delete_url(self):
        return reverse('admin_panel:delete_cinema_hall', args=[self.pk])
