# Generated by Django 5.0.2 on 2024-03-23 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0006_alter_asic_bg_fon'),
    ]

    operations = [
        migrations.AddField(
            model_name='asic',
            name='faovarit',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='В избранном'),
        ),
    ]
