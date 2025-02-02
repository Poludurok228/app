# Generated by Django 5.0.6 on 2024-06-09 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0014_asic_grivn_calc_alter_stabilizer_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='asicdescription',
            name='our_en',
            field=models.TextField(null=True, verbose_name='О товаре'),
        ),
        migrations.AddField(
            model_name='asicdescription',
            name='our_ru',
            field=models.TextField(null=True, verbose_name='О товаре'),
        ),
        migrations.AddField(
            model_name='asicdescription',
            name='our_uk',
            field=models.TextField(null=True, verbose_name='О товаре'),
        ),
        migrations.AddField(
            model_name='asicdescription',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Название Асика для описания'),
        ),
        migrations.AddField(
            model_name='asicdescription',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Название Асика для описания'),
        ),
        migrations.AddField(
            model_name='asicdescription',
            name='title_uk',
            field=models.CharField(max_length=100, null=True, verbose_name='Название Асика для описания'),
        ),
    ]
