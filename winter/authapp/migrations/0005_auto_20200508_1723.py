# Generated by Django 2.2.10 on 2020-05-08 17:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_auto_20200508_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key',
            field=models.CharField(blank=True, max_length=128, verbose_name='Ключ активации'),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 10, 17, 23, 4, 7596, tzinfo=utc), verbose_name='Время жизни ключа'),
        ),
    ]
