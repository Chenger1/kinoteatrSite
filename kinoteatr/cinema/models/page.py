from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator

from cinema.models.seo import Seo
from cinema.models.mixin import SingletonModel
from cinema.models.cinema import Cinema


class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    main_image = models.ImageField(upload_to='news/main_images/')
    url = models.URLField()
    publication_date = models.DateField()
    status = models.BooleanField()

    seo = models.ForeignKey(Seo, related_name='news', on_delete=models.CASCADE, blank=True, null=True)

    def get_images(self):
        return [self.main_image.path]

    def get_delete_url(self):
        return reverse('admin_panel:delete_news_admin', args=[self.pk])

    def __str__(self):
        return self.title


class Ad(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    main_image = models.ImageField(upload_to='ad/main_images/')
    url = models.URLField()
    publication_date = models.DateField()
    status = models.BooleanField()

    seo = models.ForeignKey(Seo, related_name='ad', on_delete=models.CASCADE, blank=True, null=True)

    def get_images(self):
        return [self.main_image.path]

    def get_delete_url(self):
        return reverse('admin_panel:delete_ad_admin', args=[self.pk])

    def __str__(self):
        return self.title


class MainPage(SingletonModel):
    phone_validation = RegexValidator(regex=r'^\+\d{8,15}$', message='Неправильный формат номера.')

    phone_number1 = models.CharField(max_length=16, validators=[phone_validation])
    phone_number2 = models.CharField(max_length=16, validators=[phone_validation])
    status = models.BooleanField(default=True)
    seo = models.ForeignKey(Seo, related_name='main_page', on_delete=models.CASCADE, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('admin_panel:edit_main_page_admin')


class Contact(models.Model):
    cinema = models.OneToOneField(Cinema, related_name='contacts', on_delete=models.CASCADE)
    address = models.TextField(blank=True)
    coord_x = models.FloatField(blank=True, null=True)
    coord_y = models.FloatField(blank=True, null=True)
    status = models.BooleanField(default=True)
    top_seo = models.BooleanField(default=False)
    seo = models.ForeignKey(Seo, related_name='contacts', on_delete=models.CASCADE, blank=True, null=True)


class AboutCinema(SingletonModel):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    main_image = models.ImageField(upload_to='about_cinema/main_images/')
    status = models.BooleanField(default=True)

    seo = models.ForeignKey(Seo, related_name='about_cinema', on_delete=models.CASCADE, blank=True, null=True)

    def get_images(self):
        return [self.main_image.path] if self.main_image else None

    def get_absolute_url(self):
        return reverse('admin_panel:edit_about_cinema_admin')

    def __str__(self):
        return self.title


class CafeBar(SingletonModel):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    main_image = models.ImageField(upload_to='cafebar/main_images/')
    status = models.BooleanField(default=True)

    seo = models.ForeignKey(Seo, related_name='cafebar', on_delete=models.CASCADE, blank=True, null=True)

    def get_images(self):
        return [self.main_image.path] if self.main_image else None

    def get_absolute_url(self):
        return reverse('admin_panel:edit_cafe_bar_admin')


class VipHall(SingletonModel):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    main_image = models.ImageField(upload_to='vip_hall/main_images/')
    status = models.BooleanField(default=True)

    seo = models.ForeignKey(Seo, related_name='vip_hall', on_delete=models.CASCADE, blank=True, null=True)

    def get_images(self):
        return [self.main_image.path] if self.main_image else None

    def get_absolute_url(self):
        return reverse('admin_panel:edit_vip_hall_admin')


class Advertisement(SingletonModel):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    main_image = models.ImageField(upload_to='Advertisement/main_images/')
    status = models.BooleanField(default=True)

    seo = models.ForeignKey(Seo, related_name='Advertisement', on_delete=models.CASCADE, blank=True, null=True)

    def get_images(self):
        return [self.main_image.path] if self.main_image else None

    def get_absolute_url(self):
        return reverse('admin_panel:edit_advertisement_admin')


class ChildRoom(SingletonModel):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    main_image = models.ImageField(upload_to='child_room/main_images/')
    status = models.BooleanField(default=True)

    seo = models.ForeignKey(Seo, related_name='child_room', on_delete=models.CASCADE, blank=True, null=True)

    def get_images(self):
        return [self.main_image.path] if self.main_image else None

    def get_absolute_url(self):
        return reverse('admin_panel:edit_child_room_admin')
