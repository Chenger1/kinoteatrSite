from django.db import models
from cinema.models.mixin import SingletonModel


class BackgroundImage(SingletonModel):
    image = models.ImageField(upload_to='background_image/')


class OnTopBanner(models.Model):
    speed_choices = [
        (1, '5s'),
        (2, '10s')
    ]

    speed = models.IntegerField(choices=speed_choices)
    status = models.BooleanField()


class SliderBanner(models.Model):
    speed_choices = [
        (1, '5s'),
        (2, '10s')
    ]

    speed = models.IntegerField(choices=speed_choices)
    status = models.BooleanField()