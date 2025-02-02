# Generated by Django 5.0.2 on 2024-03-03 18:55

import cat.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AsicBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название бренда')),
                ('image', models.FileField(upload_to='brand/', verbose_name='Фото для бренда(svg)')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
            },
        ),
        migrations.CreateModel(
            name='AsicDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название Асика для описания')),
                ('our', models.TextField(verbose_name='Обзор')),
                ('el', models.TextField(verbose_name='Энергоэффективность')),
                ('protect', models.TextField(verbose_name='Прочность и надежность')),
                ('firm', models.TextField(verbose_name='О производителе')),
                ('money', models.TextField(verbose_name='Доходность')),
            ],
            options={
                'verbose_name': 'Описание',
                'verbose_name_plural': 'Описание',
            },
        ),
        migrations.CreateModel(
            name='AsicDetailPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название асика для фото')),
                ('img', models.FileField(upload_to=cat.models.asic_detail_directory_path, verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фото',
            },
        ),
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Название монеты')),
            ],
            options={
                'verbose_name': 'Монета',
                'verbose_name_plural': 'Монеты',
            },
        ),
        migrations.CreateModel(
            name='FastFilter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название фильтра')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Быстрый фильтер',
                'verbose_name_plural': 'Быстрые фильтры',
            },
        ),
        migrations.CreateModel(
            name='MiniProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название Асика для характеристик')),
                ('algo', models.CharField(max_length=100, verbose_name='Алгоритм')),
                ('coin', models.CharField(max_length=100, verbose_name='Добываемые(ая) монеты(а)')),
                ('electro', models.CharField(max_length=100, verbose_name='Энергопотребление, пример: 3 080 Вт/ч ± 5%')),
            ],
            options={
                'verbose_name': 'Мини характеристика',
                'verbose_name_plural': 'Мини характеристики',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название Асика для характеристик')),
                ('firm', models.CharField(max_length=255, verbose_name='Производитель')),
                ('model', models.CharField(max_length=20, verbose_name='Модель')),
                ('crpt', models.CharField(max_length=100, verbose_name='Криптовалюта(ы)')),
                ('hesh', models.CharField(max_length=100, verbose_name='Хешрэйт, пример: 63,5 Th/s')),
                ('algo', models.CharField(max_length=100, verbose_name='Алгоритм')),
                ('coin', models.CharField(max_length=100, verbose_name='Добываемые(ая) монеты(а)')),
                ('electro', models.CharField(max_length=100, verbose_name='Энергопотребление, пример: 3 080 Вт/ч ± 5%')),
                ('elect_ef', models.CharField(max_length=100, verbose_name='Энергоэффективность, пример: 48 J/TH')),
                ('temp', models.CharField(max_length=255, verbose_name='Рабочая температура, пример: от 0 до 40 °С')),
                ('power', models.CharField(max_length=100, verbose_name='Источник питания')),
                ('cold', models.CharField(max_length=100, verbose_name='Охлаждение')),
                ('size', models.CharField(max_length=255, verbose_name='Размеры, пример: 195х290х400 мм')),
                ('nose', models.CharField(max_length=100, verbose_name='Уровень шума, пример: 75 дБ')),
            ],
            options={
                'verbose_name': 'Характеристика',
                'verbose_name_plural': 'Характеристики',
            },
        ),
        migrations.CreateModel(
            name='Asic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Полное название Асика')),
                ('title_min', models.CharField(max_length=255, verbose_name='Краткое название Асика')),
                ('asic_number', models.PositiveIntegerField(default=0, verbose_name='Номер асика')),
                ('main_img', models.ImageField(upload_to=cat.models.asic_directory_path, verbose_name='Главное фото Асика')),
                ('hesh', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Хешрэйт, пример: 65.6')),
                ('power', models.PositiveIntegerField(default=0, verbose_name='Потребление, пример: 3200')),
                ('price', models.DecimalField(decimal_places=0, max_digits=8, verbose_name='Цена')),
                ('old_price', models.DecimalField(blank=True, decimal_places=0, max_digits=8, null=True, verbose_name='Старая Цена (если есть)')),
                ('active', models.BooleanField(default=True, verbose_name='Активный')),
                ('availability', models.BooleanField(default=True, verbose_name='Наличие')),
                ('popular', models.BooleanField(default=False, verbose_name='Популярный асик')),
                ('article', models.BigIntegerField(default=cat.models.generate_random_number, verbose_name='Артикул')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cat.asicbrand', verbose_name='Бренд Асика')),
                ('description', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='cat.asicdescription', verbose_name='Описание')),
                ('detail_img', models.ManyToManyField(to='cat.asicdetailphoto', verbose_name='Фото асика для слайдера(детальная страница)')),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cat.coin', verbose_name='Основная добываемая монета')),
                ('mini_property', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='cat.miniproperty', verbose_name='Мини Характеристики')),
                ('property', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='cat.property', verbose_name='Основные Характеристики')),
            ],
            options={
                'verbose_name': 'Асик',
                'verbose_name_plural': 'Асики',
            },
        ),
    ]
