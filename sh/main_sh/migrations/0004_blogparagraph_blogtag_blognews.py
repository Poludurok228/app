# Generated by Django 5.0.2 on 2024-03-20 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_sh', '0003_slide_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogParagraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок абзаца')),
                ('text', models.TextField(verbose_name='Текст абзаца')),
            ],
            options={
                'verbose_name': 'Абзац',
                'verbose_name_plural': 'Абзацы',
            },
        ),
        migrations.CreateModel(
            name='BlogTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='BlogNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок новости')),
                ('description', models.TextField(verbose_name='Описание новости')),
                ('img', models.ImageField(upload_to='news/', verbose_name='Фото для новости(желательно 16:9, хуй знает как другая выглядеть будет)')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('publish', models.BooleanField(default=True, verbose_name='Опубликован')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('paragraphs', models.ManyToManyField(to='main_sh.blogparagraph', verbose_name='Параграфы для новости')),
                ('tegs', models.ManyToManyField(to='main_sh.blogtag', verbose_name='Теги для новости(любые, похуй)')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
