from django.db import models

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


class Ad(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    main_image = models.ImageField(upload_to='ad/main_images/')
    url = models.URLField()
    publication_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()

    seo = models.ForeignKey(Seo, related_name='ad', on_delete=models.CASCADE, blank=True, null=True)

    def get_images(self):
        return [self.main_image.path]


class MainPage(SingletonModel):
    phone_number1 = models.CharField(max_length=30)
    phone_number2 = models.CharField(max_length=30)
    status = models.BooleanField()
    seo = models.ForeignKey(Seo, related_name='main_page', on_delete=models.CASCADE, blank=True, null=True)


class Contact(SingletonModel):
    cinema = models.ForeignKey(Cinema, related_name='contacts', on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    coord_x = models.FloatField()
    coord_y = models.FloatField()
    seo = models.ForeignKey(Seo, related_name='contacts', on_delete=models.CASCADE, blank=True, null=True)


class AboutCinema(SingletonModel):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    main_image = models.ImageField(upload_to='about_cinema/main_images/')
    url = models.URLField()
    status = models.BooleanField()

    seo = models.ForeignKey(Seo, related_name='about_cinema', on_delete=models.CASCADE, blank=True, null=True)

    def get_images(self):
        return [self.image.path] if self.image else None


class CafeBar(SingletonModel):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    main_image = models.ImageField(upload_to='cafebar/main_images/')
    url = models.URLField()
    status = models.BooleanField()

    seo = models.ForeignKey(Seo, related_name='cafebar', on_delete=models.CASCADE, blank=True, null=True)

    def get_images(self):
        return [self.image.path] if self.image else None


class VipHall(SingletonModel):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    main_image = models.ImageField(upload_to='vip_hall/main_images/')
    url = models.URLField()
    status = models.BooleanField()

    seo = models.ForeignKey(Seo, related_name='vip_hall', on_delete=models.CASCADE, blank=True, null=True)

    def get_images(self):
        return [self.image.path] if self.image else None


class Advertisement(SingletonModel):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    main_image = models.ImageField(upload_to='Advertisement/main_images/')
    url = models.URLField()
    status = models.BooleanField()

    seo = models.ForeignKey(Seo, related_name='Advertisement', on_delete=models.CASCADE, blank=True, null=True)

    def get_images(self):
        return [self.image.path] if self.image else None


class ChildRoom(SingletonModel):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    main_image = models.ImageField(upload_to='child_room/main_images/')
    url = models.URLField()
    status = models.BooleanField()

    seo = models.ForeignKey(Seo, related_name='child_room', on_delete=models.CASCADE, blank=True, null=True)

    def get_images(self):
        return [self.image.path] if self.image else None
