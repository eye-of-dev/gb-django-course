# Generated by Django 2.2.10 on 2020-04-18 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзина'},
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Колличество'),
        ),
    ]