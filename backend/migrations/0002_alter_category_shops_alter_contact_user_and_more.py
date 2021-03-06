# Generated by Django 4.0.4 on 2022-05-24 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='shops',
            field=models.ManyToManyField(blank=True, null=True, related_name='categories', to='backend.shop', verbose_name='Магазины'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ordered_items', to='backend.order', verbose_name='Заказ'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ordered_items', to='backend.productinfo', verbose_name='Информация о продукте'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='backend.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='model',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_infos', to='backend.product', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='shop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_infos', to='backend.shop', verbose_name='Магазин'),
        ),
        migrations.AlterField(
            model_name='productparameter',
            name='parameter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_parameters', to='backend.parameter', verbose_name='Параметр'),
        ),
        migrations.AlterField(
            model_name='productparameter',
            name='product_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_parameters', to='backend.productinfo', verbose_name='Информация о продукте'),
        ),
    ]
