from django.db import models

from cinema.models.movie import Movie
from cinema.models.page import News, Ad, AboutCinema, CafeBar, VipHall, Advertisement, ChildRoom
from cinema.models.cinema import Cinema
from cinema.models.banners import OnTopBanner, SliderBanner


def get_movie_gallery_image_path(instance, filename):
    return f'movie/{instance.movie.name}/gallery/{filename}'


def get_cinema_gallery_image_path(instance, filename):
    return f'cinema/{instance.cinema.name}/gallery/{filename}'


class MovieGallery(models.Model):
    entity = models.ForeignKey(Movie, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_movie_gallery_image_path)


class NewsGallery(models.Model):
    entity = models.ForeignKey(News, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news/gallery/')


class AdsGallery(models.Model):
    entity = models.ForeignKey(Ad, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ads/gallery/')


class AboutCinemaGallery(models.Model):
    entity = models.ForeignKey(AboutCinema, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='about_cinema/gallery/')


class CafeBarGallery(models.Model):
    entity = models.ForeignKey(CafeBar, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cafebar/gallery/')


class VipHallGallery(models.Model):
    entity = models.ForeignKey(VipHall, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='vip_hall/gallery/')


class AdvertisementGallery(models.Model):
    entity = models.ForeignKey(Advertisement, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='advertisement/gallery/')


class ChildRoomGallery(models.Model):
    entity = models.ForeignKey(ChildRoom, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='child_room/gallery/')


class CinemaGallery(models.Model):
    entity = models.ForeignKey(Cinema, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_cinema_gallery_image_path)


class SliderBannerGallery(models.Model):
    entity = models.ForeignKey(SliderBanner, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='slider_banner/gallery/')
    url = models.URLField()


class OnTopBannerGallery(models.Model):
    entity = models.ForeignKey(OnTopBanner, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='on_top_banner/gallery/')
    url = models.URLField()
    text = models.CharField(max_length=150, blank=True)
