from cinema.models.mixin import SingletonModel

from cinema.models.receiver import *


class BackgroundImage(SingletonModel):
    image = models.ImageField(upload_to='background_image/', null=True)
    status = models.BooleanField(default=False)


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
