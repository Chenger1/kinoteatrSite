from django.db import models
from cinema.models.mixin import SingletonModel
from django_resized import ResizedImageField


class BackgroundImage(SingletonModel):
    image = ResizedImageField(size=[2000, 3000], quality=100, upload_to='background_image/')


class OnTopBanner(SingletonModel):
    speed_choices = [
        (1, '5s'),
        (2, '10s')
    ]

    speed = models.IntegerField(choices=speed_choices, default=1)
    status = models.BooleanField(default=True)


class SliderBanner(SingletonModel):
    speed_choices = [
        (1, '5s'),
        (2, '10s')
    ]

    speed = models.IntegerField(choices=speed_choices, default=1)
    status = models.BooleanField(default=True)
