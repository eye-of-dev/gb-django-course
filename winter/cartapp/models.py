from django.conf import settings
from django.db import models
from django.db.models import Avg, Sum

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

    @property
    def total_price_by_row(self):
        return self.price * self.quantity


class CartCommon:
    """
    Объект для работы с корзиной
    """

    def __init__(self, cart_uuid):
        self.cart_uuid = cart_uuid

    def get_user_products(self):
        """
        Получаем все продукты, которые пользователь добавил в корзину
        :return:
        """
        return Cart.objects.filter(cart_uuid=self.cart_uuid).all()

    @property
    def total_cart_unique_products(self):
        """
        Получаем колличество уникальных продуктов в корзине
        :return:
        """
        return Cart.objects.filter(cart_uuid=self.cart_uuid).count()

    @property
    def total_cart_all_products(self):
        """
        Получаем общее колличество товаров в корзине
        :return:
        """
        count_products = Cart.objects.filter(cart_uuid=self.cart_uuid).aggregate(Sum('quantity'))
        if count_products['quantity__sum']:
            return count_products['quantity__sum']

        return 0

    @property
    def total_cart_price_products(self):
        """
        Получаем сумму товаров в корзине
        :return:
        """
        total = 0
        products = self.get_user_products()
        for product in products:
            total += product.quantity * product.price

        return total
