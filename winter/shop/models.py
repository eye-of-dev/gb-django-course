"""
    Models shop app
"""
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class ProductCategories(models.Model):
    """
        Product categories class
    """
    title = models.CharField('Название категории', max_length=128, unique=True)
    short_description = models.CharField('Краткое описание', max_length=255, null=True, blank=True)
    is_active = models.BooleanField('Статус', default=0)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title

    @property
    def list_products(self):
        return Products.objects.filter(category=self.id).all()


class Products(models.Model):
    """
        Product categories class
    """
    category = models.ForeignKey(ProductCategories, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField('Название продукта', max_length=128, unique=True)
    image = models.ImageField('Изображение продукта', upload_to='products_images', blank=True)
    short_description = models.CharField('Краткое описание', max_length=255, null=True, blank=True)
    description = models.TextField('Описание продукта', null=True, blank=True)
    price = models.DecimalField('Цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.IntegerField('Колличество на складе', default=0)
    is_active = models.BooleanField('Статус', default=0)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = "Товары"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.title

    @receiver(pre_save, sender=ProductCategories)
    def product_is_active_update_productcategory_save(sender, instance, **kwargs):
        if instance.pk:
            if instance.is_active:
                instance.list_products.update(is_active=True)
            else:
                instance.list_products.update(is_active=False)
