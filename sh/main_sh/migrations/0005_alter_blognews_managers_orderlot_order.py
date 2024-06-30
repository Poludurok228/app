# Generated by Django 5.0.2 on 2024-03-21 06:11

import django.db.models.deletion
import django.db.models.manager
import main_sh.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0006_alter_asic_bg_fon'),
        ('main_sh', '0004_blogparagraph_blogtag_blognews'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='blognews',
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='OrderLot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Для какого заказа, пример: Лот для заказа 1')),
                ('number', models.PositiveIntegerField(default=1, verbose_name='Номер лота (в списке)')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество асиков в лоте')),
                ('asic', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cat.asic', verbose_name='Асик для лота')),
            ],
            options={
                'verbose_name': 'Лот',
                'verbose_name_plural': 'Лоты',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Номер заказа, например: Заказ 1')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('order_number', models.BigIntegerField(default=main_sh.models.generate_random_number, verbose_name='Номер заказа')),
                ('in_processing', models.BooleanField(default=True, verbose_name='В обработке')),
                ('in_assembly', models.BooleanField(default=False, verbose_name='В сборке')),
                ('in_transit', models.BooleanField(default=False, verbose_name='В пути')),
                ('ready', models.BooleanField(default=False, verbose_name='Готов к выдаче')),
                ('delivery_date', models.DateTimeField(verbose_name='Дата доставки(ну +-, или на которую договорились)')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('order_lots', models.ManyToManyField(to='main_sh.orderlot', verbose_name='Пункты в заказе')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
