# Generated by Django 4.1.5 on 2023-02-26 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0004_gallery_participant_alter_champion_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='champion',
            options={'verbose_name': 'Чемпион турнира', 'verbose_name_plural': 'Чемпионы турниров'},
        ),
    ]
