# Generated by Django 4.1.5 on 2023-02-26 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0005_alter_champion_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'Изображение галереи', 'verbose_name_plural': 'Изображения галереи'},
        ),
        migrations.AddField(
            model_name='gallery',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата создания новости'),
        ),
    ]
