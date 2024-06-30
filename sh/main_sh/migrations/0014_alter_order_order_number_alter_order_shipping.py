# Generated by Django 5.0.2 on 2024-04-09 06:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_sh', '0013_orderlot_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.BigIntegerField(unique=True, verbose_name='Номер заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_sh.shipping', verbose_name='Информация по доставке'),
        ),
    ]
