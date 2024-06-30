# Generated by Django 5.0.2 on 2024-03-08 22:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asic',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создан'),
        ),
        migrations.AddField(
            model_name='asic',
            name='percentages',
            field=models.DecimalField(blank=True, decimal_places=1, default=1, max_digits=4, null=True, verbose_name='Различие дохода в процентах, пример: 0.8'),
        ),
        migrations.AddField(
            model_name='asic',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Изменён'),
        ),
        migrations.AlterField(
            model_name='asic',
            name='description',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cat.asicdescription', verbose_name='Описание'),
        ),
    ]
