from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.core.validators import RegexValidator

from cinema.models.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    language_choices = [
        (0, 'Русский'),
        (1, 'Украинский')
    ]
    gender_choices = [
        (0, 'Мужской'),
        (1, 'Женский')
    ]
    phone_validation = RegexValidator(regex=r'^\+\d{8,15}$', message='Неправильный формат номера.')

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50, validators=[phone_validation])

    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=150, blank=True)
    card_number = models.CharField(max_length=50, blank=True)
    language = models.IntegerField(choices=language_choices, default=0)
    gender = models.IntegerField(choices=gender_choices, blank=True, null=True)
    birthday_date = models.DateTimeField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'username']

    objects = UserManager()

    @property
    def get_birthday_date(self):
        return self.birthday_date.strftime('%d.%m.%Y') if self.birthday_date else ''

    @property
    def get_joined_date(self):
        return self.date_joined.strftime('%d.%m.%Y')

    def __str__(self):
        return self.username
