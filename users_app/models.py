from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.CharField(unique=True, verbose_name='E-mail')
    phone = models.CharField(max_length=35, **NULLABLE, verbose_name='Контактный телефон')
    country = models.CharField(max_length=150, **NULLABLE, verbose_name='Страна')
    avatar = models.ImageField(upload_to='media/user_avatars', **NULLABLE, verbose_name='Аватар')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
