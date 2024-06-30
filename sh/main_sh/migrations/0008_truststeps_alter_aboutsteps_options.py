# Generated by Django 5.0.2 on 2024-03-22 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_sh', '0007_aboutsteps'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrustSteps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.AlterModelOptions(
            name='aboutsteps',
            options={'ordering': ['pk']},
        ),
    ]
