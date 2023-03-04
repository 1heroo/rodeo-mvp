from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование новости')
    body = models.TextField(verbose_name='Описание новости')
    image = models.ImageField(upload_to='news/%Y/%m/%d/', verbose_name='Изображение новости')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания новости')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']
