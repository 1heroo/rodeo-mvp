from django.db import models
from users.models import MyUser


class Participant(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    bio = models.TextField(verbose_name='Описание')
    avatar = models.ImageField(upload_to='avatars/', verbose_name='Фото участника', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Участик турнира'
        verbose_name_plural = "Участники турниров"


class Tournament(models.Model):
    title = models.CharField(max_length=256, verbose_name='Наименование турнира')
    description = models.TextField(verbose_name='Описание турнира')
    date = models.DateTimeField(verbose_name='Дата проведения')
    participants = models.ManyToManyField(to=Participant, related_name='tournaments', blank=True, verbose_name='Участники')
    image = models.ImageField(upload_to='tournament/%Y/%m/%d/', verbose_name='Изображение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Турнир'
        verbose_name_plural = "Турниры"


class Champion(models.Model):
    champion = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='champions', verbose_name='Чемпион')
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='champions', verbose_name='Турнир')

    def __str__(self):
        return self.champion.first_name

    class Meta:
        verbose_name = 'Чемпион турнира'
        verbose_name_plural = "Чемпионы турниров"


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/%Y/%m/%d/', verbose_name='Изображение в галерея')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания новости')

    def __str__(self):
        return 'Изображение'

    class Meta:
        verbose_name = 'Изображение галереи'
        verbose_name_plural = "Изображения галереи"
        ordering = ['-created_at']