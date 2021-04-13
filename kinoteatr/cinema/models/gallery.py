from django.db import models
from django.urls import reverse

from cinema.models.movie import Movie
from cinema.models.page import News, Ad, AboutCinema, CafeBar, VipHall, Advertisement, ChildRoom
from cinema.models.cinema import Cinema, CinemaHall
from cinema.models.banners import OnTopBanner, SliderBanner


def get_movie_gallery_image_path(instance, filename):
    return f'movie/{instance.entity.name}/gallery/{filename}'


def get_cinema_gallery_image_path(instance, filename):
    return f'cinema/{instance.entity.name}/gallery/{filename}'


def get_cinema_hall_gallery_image_path(instance, filename):
    return f'cinema_hall/{instance.entity.number}/gallery/{filename}'


class MovieGallery(models.Model):
    entity = models.ForeignKey(Movie, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_movie_gallery_image_path)

    def get_images(self):
        return [self.image.path]

    def get_delete_url(self):
        return reverse('admin_panel:delete_movie_gallery_image_admin', args=[self.pk])


class NewsGallery(models.Model):
    entity = models.ForeignKey(News, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news/gallery/')

    def get_images(self):
        return [self.image.path]

    def get_delete_url(self):
        return reverse('admin_panel:delete_news_gallery_image_admin', args=[self.pk])


class AdsGallery(models.Model):
    entity = models.ForeignKey(Ad, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ads/gallery/')

    def get_images(self):
        return [self.image.path]


class AboutCinemaGallery(models.Model):
    entity = models.ForeignKey(AboutCinema, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='about_cinema/gallery/')

    def get_images(self):
        return [self.image.path]


class CafeBarGallery(models.Model):
    entity = models.ForeignKey(CafeBar, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cafebar/gallery/')

    def get_images(self):
        return [self.image.path]


class VipHallGallery(models.Model):
    entity = models.ForeignKey(VipHall, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='vip_hall/gallery/')

    def get_images(self):
        return [self.image.path]


class AdvertisementGallery(models.Model):
    entity = models.ForeignKey(Advertisement, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='advertisement/gallery/')

    def get_images(self):
        return [self.image.path]


class ChildRoomGallery(models.Model):
    entity = models.ForeignKey(ChildRoom, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='child_room/gallery/')

    def get_images(self):
        return [self.image.path]


class CinemaGallery(models.Model):
    entity = models.ForeignKey(Cinema, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_cinema_gallery_image_path)

    def get_images(self):
        return [self.image.path]

    def get_delete_url(self):
        return reverse('admin_panel:delete_cinema_gallery_image', args=[self.pk])


class CinemaHallGallery(models.Model):
    entity = models.ForeignKey(CinemaHall, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_cinema_hall_gallery_image_path)

    def get_images(self):
        return [self.image.path]

    def get_delete_url(self):
        return reverse('admin_panel:delete_cinema_hall_gallery_image', args=[self.pk])


class SliderBannerGallery(models.Model):
    entity = models.ForeignKey(SliderBanner, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='slider_banner/gallery/')
    url = models.URLField(blank=True, null=True)

    def get_images(self):
        return [self.image.path]


class OnTopBannerGallery(models.Model):
    entity = models.ForeignKey(OnTopBanner, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='on_top_banner/gallery/')
    url = models.URLField(blank=True, null=True)
    text = models.CharField(max_length=150, blank=True)

    def get_images(self):
        return [self.image.path]
