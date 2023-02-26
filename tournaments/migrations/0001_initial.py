# Generated by Django 4.1.5 on 2023-02-26 08:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='uploads/%Y/%m/%d/')),
                ('participants', models.ManyToManyField(blank=True, related_name='tournaments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]