from django.db import models
from django.urls import reverse

from cinema.models.movie import Movie
from cinema.models.page import News, Ad, AboutCinema, CafeBar, VipHall, Advertisement, ChildRoom, MobileApp
from cinema.models.cinema import Cinema, CinemaHall
from cinema.models.banners import OnTopBanner, SliderBanner
from cinema.utils.get_valid_dir_name import get_valid_dir_name


def get_movie_gallery_image_path(instance, filename):
    name = get_valid_dir_name(instance.entity.name)
    return f'movie/{name}/gallery/{filename}'


def get_cinema_gallery_image_path(instance, filename):
    name = get_valid_dir_name(instance.entity.name)
    return f'cinema/{name}/gallery/{filename}'


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
    image = models.ImageField(upload_to='ad/gallery/')

    def get_images(self):
        return [self.image.path]

    def get_delete_url(self):
        return reverse('admin_panel:delete_ad_gallery_image_admin', args=[self.pk])


class AboutCinemaGallery(models.Model):
    entity = models.ForeignKey(AboutCinema, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='about_cinema/gallery/')

    def get_images(self):
        return [self.image.path]

    def get_delete_url(self):
        return reverse('admin_panel:delete_about_cinema_gallery_image', args=[self.pk])


class CafeBarGallery(models.Model):
    entity = models.ForeignKey(CafeBar, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cafebar/gallery/')

    def get_images(self):
        return [self.image.path]

    def get_delete_url(self):
        return reverse('admin_panel:delete_cafe_bar_gallery_image', args=[self.pk])


class VipHallGallery(models.Model):
    entity = models.ForeignKey(VipHall, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='vip_hall/gallery/')

    def get_images(self):
        return [self.image.path]

    def get_delete_url(self):
        return reverse('admin_panel:delete_vip_hall_gallery_image', args=[self.pk])


class AdvertisementGallery(models.Model):
    entity = models.ForeignKey(Advertisement, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='advertisement/gallery/')

    def get_images(self):
        return [self.image.path]

    def get_delete_url(self):
        return reverse('admin_panel:delete_advertisement_gallery_image', args=[self.pk])


class ChildRoomGallery(models.Model):
    entity = models.ForeignKey(ChildRoom, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='child_room/gallery/')

    def get_images(self):
        return [self.image.path]

    def get_delete_url(self):
        return reverse('admin_panel:delete_child_room_gallery_image', args=[self.pk])


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


class MobileAppGallery(models.Model):
    entity = models.ForeignKey(MobileApp, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='mobile_app/gallery/')

    def get_images(self):
        return [self.image.path]

    def get_delete_url(self):
        return reverse('admin_panel:delete_mobile_app_gallery_image', args=[self.pk])
