from django.conf import settings
from django.db import models

from shop.models import Products


class WishList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(Products, verbose_name='Продукт', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'product')
