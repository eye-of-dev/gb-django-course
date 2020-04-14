from django.conf import settings
from django.db import models

from shop.models import Products


class Cart(models.Model):
    cart_uuid = models.CharField('Идентификатор корзины', max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', null=True,
                             blank=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.PositiveSmallIntegerField('Колличество', default=0)
    price = models.DecimalField('Цена продукта', max_digits=8, decimal_places=2, default=0)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"

    def __str__(self):
        return self.product.title
