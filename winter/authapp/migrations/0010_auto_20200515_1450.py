# Generated by Django 2.2.10 on 2020-05-15 14:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0009_auto_20200512_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 17, 14, 50, 8, 593201, tzinfo=utc), verbose_name='Время жизни ключа'),
        ),
    ]
