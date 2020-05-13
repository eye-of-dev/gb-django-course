from django.db import models

import winter.settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from shop.models import Products


class Order(models.Model):
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


class OrderUserInfo(models.Model):
    order = models.OneToOneField(Order, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30)
    email = models.CharField('E-mail', max_length=255)

    @receiver(post_save, sender=Order)
    def create_order_user_info(sender, instance, created, **kwargs):
        if created:
            OrderUserInfo.objects.create(order=instance)

    @receiver(post_save, sender=Order)
    def save_order_user_info(sender, instance, **kwargs):
        instance.orderuserinfo.save()


class OrderProducts(models.Model):
    order = models.ForeignKey(Order, verbose_name='Заказ', related_name='orderproducts', db_index=True,
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Products, verbose_name='Продукт', db_index=True, on_delete=models.DO_NOTHING)
    quantity = models.PositiveSmallIntegerField('Колличество', default=0)
    price = models.DecimalField('Цена продукта', max_digits=8, decimal_places=2, default=0)
