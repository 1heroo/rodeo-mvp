from django.db import models


class Ticket(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название билета?')
    description = models.TextField(verbose_name='Описание билета')
    price = models.PositiveIntegerField(verbose_name='Цена билета')
    image = models.ImageField(upload_to='ticket/', verbose_name='Изображение мест на стадионе')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = "Билеты"
