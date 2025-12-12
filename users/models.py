

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True,blank=True,null=True,verbose_name='Имя пользователя')
    email = models.EmailField(unique=True, verbose_name="Email Address")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Телефон")
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name="Город")
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True, verbose_name="Аватарка")


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']


class Payment(models.Model):
    # Cпособы оплаты
    PAYMENT_CHOICES = [
        ('cash', 'Наличные'),
        ('transfer', 'Перевод на счет')
    ]

    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Пользователь')
    payment_date = models.DateTimeField(default=timezone.now, verbose_name='Дата оплаты')
    course = models.ForeignKey('materials.Course', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Оплаченный курс')
    lesson = models.ForeignKey('materials.Lesson', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Оплаченный урок')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма оплаты')
    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES, verbose_name='Cпособ оплаты')

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'


