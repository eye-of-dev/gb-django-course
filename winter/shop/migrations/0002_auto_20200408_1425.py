# Generated by Django 2.2.10 on 2020-04-08 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategories',
            options={'verbose_name': 'Категории', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterField(
            model_name='productcategories',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='productcategories',
            name='short_description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='productcategories',
            name='title',
            field=models.CharField(max_length=128, unique=True, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='productcategories',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True, verbose_name='Название продукта')),
                ('image', models.ImageField(blank=True, upload_to='products_images', verbose_name='Изображение продукта')),
                ('short_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Краткое описание')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание продукта')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Цена продукта')),
                ('quantity', models.IntegerField(default=0, verbose_name='Колличество на складе')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.ProductCategories')),
            ],
            options={
                'verbose_name': 'Товары',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]