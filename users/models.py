from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None


email = models.EmailField(unique=True, verbose_name="Email Address")
phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Телефон")
city = models.CharField(max_length=50, blank=True, null=True, verbose_name="Город")
avatar = models.ImageField(upload_to="avatars/", blank=True, null=True, verbose_name="Аватарка")



USERNAME_FIELD = "email"
REQUIRED_FIELDS = []
