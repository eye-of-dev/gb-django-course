from django.db import models

import winter.settings
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from shop.models import Products


class Orders(models.Model):
    FORMING = 'FM'
    SENT_TO_PROCEED = 'STP'
    PROCEEDED = 'PRD'
    PAID = 'PD'
    READY = 'RDY'
    CANCEL = 'CNC'

    ORDER_STATUS_CHOICES = (
        (FORMING, 'Формируется'),
        (SENT_TO_PROCEED, 'Отправлен в обработку'),
        (PROCEEDED, 'Обрабатывается'),
        (PAID, 'Оплачен'),
        (READY, 'Готов к выдаче'),
        (CANCEL, 'Отменен'),
    )

    user = models.ForeignKey(winter.settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь',
                             null=True, blank=True)
    total = models.DecimalField('Сумма заказа', max_digits=8, decimal_places=2, default=0)
    status = models.CharField('Статус заказа', max_length=3, choices=ORDER_STATUS_CHOICES, default=SENT_TO_PROCEED)
    comment = models.TextField('Комментарий', max_length=512, blank=True, null=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    @property
    def get_orders_products(self):
        """
        Товары в заказе
        :return:
        """
        return OrdersProducts.objects.filter(order=self).all()

    @property
    def get_count_products(self):
        """
        Колличество продуктов в заказе
        :return:
        """
        total = 0
        products = self.get_orders_products
        for product in products:
            total += product.quantity

        return total


class OrdersUserInfo(models.Model):
    order = models.OneToOneField(Orders, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30)
    email = models.CharField('E-mail', max_length=255)

    @property
    def user_name(self):
        return f'{self.first_name} {self.last_name} - ({self.email})'

    @receiver(post_save, sender=Orders)
    def create_order_user_info(sender, instance, created, **kwargs):
        if created:
            OrdersUserInfo.objects.create(order=instance)

    @receiver(post_save, sender=Orders)
    def save_order_user_info(sender, instance, **kwargs):
        instance.ordersuserinfo.save()


class OrdersProducts(models.Model):
    order = models.ForeignKey(Orders, verbose_name='Заказ', related_name='orderproducts', db_index=True,
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Products, verbose_name='Продукт', db_index=True, on_delete=models.DO_NOTHING)
    quantity = models.PositiveSmallIntegerField('Колличество', default=0)
    price = models.DecimalField('Цена продукта', max_digits=8, decimal_places=2, default=0)

    def get_item(pk):
        return OrdersProducts.objects.get(pk=pk)

    def save(self, *args, **kwargs):
        if self.pk:
            self.product.quantity -= self.quantity - self.__class__.get_item(self.pk).quantity
        else:
            self.product.quantity -= self.quantity
        self.product.save()
        super(self.__class__, self).save(*args, **kwargs)
