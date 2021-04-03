from django.db import models

from cinema.models.seo import Seo


def get_main_image_path(instance, filename):
    return f'movie/{instance.name}/main_image/{filename}'


class Movie(models.Model):
    status_choices = [
        (1, 'Released'),
        (0, 'Soon')
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    main_image = models.ImageField(upload_to=get_main_image_path)
    url = models.URLField()
    is_2d = models.BooleanField(default=False)
    is_3d = models.BooleanField(default=False)
    is_imax = models.BooleanField(default=False)
    status = models.IntegerField(choices=status_choices, default=0)
    release = models.DateTimeField()
    seo_id = models.ForeignKey(Seo, related_name='movies', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'movie'


class ExtendedInfo(models.Model):
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

    movie = models.OneToOneField(Movie, related_name='info', on_delete=models.CASCADE)
    language = models.IntegerField(choices=language_choices)
    director = models.CharField(max_length=100)
    running_time = models.TimeField()
    country = models.CharField(max_length=100)
    genre = models.IntegerField(choices=genre_choices)
    age_limit = models.IntegerField(choices=age_limit_choices)

    class Meta:
        db_table = 'extended_info'
