# Generated by Django 5.0.2 on 2024-04-08 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_sh', '0011_order_shipping'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
