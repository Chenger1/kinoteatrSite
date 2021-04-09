from django.db import models

from embed_video.fields import EmbedVideoField

from cinema.models.seo import Seo


def get_main_image_path(instance, filename):
    return f'movie/{instance.name}/main_image/{filename}'


class Movie(models.Model):
    language_choices = [
        (1, 'Русский'),
        (2, 'Украинский'),
        (3, 'Английский')
    ]
    genre_choices = [
        (1, 'Comedy'),
        (2, 'Horror'),
        (3, 'Action'),
        (4, 'Thriller'),
        (5, 'Adventure')
    ]

    age_limit_choices = [
        (1, '<18'),
        (2, '>18')
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    main_image = models.ImageField(upload_to=get_main_image_path)
    url = EmbedVideoField()
    is_2d = models.BooleanField(default=False)
    is_3d = models.BooleanField(default=False)
    is_imax = models.BooleanField(default=False)
    released = models.BooleanField(default=False)
    release = models.DateField()
    language = models.IntegerField(choices=language_choices)
    director = models.CharField(max_length=100)
    running_time = models.TimeField()
    country = models.CharField(max_length=100)
    genre = models.IntegerField(choices=genre_choices)
    age_limit = models.IntegerField(choices=age_limit_choices)
    seo = models.ForeignKey(Seo, related_name='movies', on_delete=models.CASCADE, blank=True, null=True)

    def get_images(self):
        return [self.main_image.path]

    def get_running_time(self):
        return self.running_time.strftime('%H:%M')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'movie'
