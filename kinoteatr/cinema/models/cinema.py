from django.db import models
from django.urls import reverse

from cinema.models.seo import Seo
from cinema.utils.get_valid_dir_name import get_valid_dir_name
from cinema.models.utils import DEFAULT_SCHEMA

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
    description = models.TextField()
    conditions = models.TextField()
    on_top_banner = models.ImageField(upload_to=get_cinema_main_image_path)
    logo = models.ImageField(upload_to=get_cinema_logo_path)
    seo = models.ForeignKey(Seo, related_name='cinema', on_delete=models.CASCADE,
                            blank=True, null=True)

    def get_images(self):
        return [self.on_top_banner.path, self.logo.path]

    def get_delete_url(self):
        return reverse('admin_panel:delete_cinema_admin', args=[self.pk])

    @property
    def next_hall_number(self):
        # increment number of the last cinema hall to get next number for new one
        last_hall = self.halls.last()
        if last_hall:
            return last_hall.number + 1
        return 1

    def __str__(self):
        return self.name


class CinemaHall(models.Model):
    cinema = models.ForeignKey(Cinema, related_name='halls', on_delete=models.CASCADE)
    number = models.IntegerField()
    description = models.TextField()
    schema = models.FileField(upload_to='cinema_hall/schema/')
    schema_json = models.TextField(default='{}')
    on_top_banner = models.ImageField(upload_to=get_hall_main_image_path)
    seats_amount = models.IntegerField(default=0)
    seo = models.ForeignKey(Seo, related_name='cinema_hall', on_delete=models.CASCADE,
                            blank=True, null=True)
    is_2d = models.BooleanField(default=True)
    is_3d = models.BooleanField(default=False)
    is_imax = models.BooleanField(default=False)

    is_vip_hall = models.BooleanField(default=False)

    creation_date = models.DateField(auto_now_add=True)

    def get_images(self):
        return [self.schema.path, self.on_top_banner.path]

    def clone_schema_json(self):
        return copy.deepcopy(self.schema_json)

    @classmethod
    def get_default_schema(cls):
        return DEFAULT_SCHEMA

    @property
    def available_formats(self):
        result = []
        if self.is_2d:
            result.append('2D')
        if self.is_3d:
            result.append('3D')
        if self.is_imax:
            result.append('IMAX')
        return ', '.join(result)

    @property
    def vip(self):
        return 'VIP' if self.is_vip_hall else ''

    def get_delete_url(self):
        return reverse('admin_panel:delete_cinema_hall', args=[self.pk])

    def get_absolute_public_url(self):
        return f'{self.pk}'
