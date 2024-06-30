# Generated by Django 5.0.2 on 2024-04-12 00:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0009_asic_usdt'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория товара',
                'verbose_name_plural': 'Категории товара',
            },
        ),
        migrations.CreateModel(
            name='Stabilizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_property', models.CharField(max_length=255, verbose_name='Уникальная характеристика')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название товара')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена товара')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cat.productcategory', verbose_name='Категория товара')),
            ],
        ),
    ]
