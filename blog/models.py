from django.conf import settings
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(**NULLABLE, verbose_name='Содержимое')
    image = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='Изображение')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Автор')
    date_created = models.DateField(**NULLABLE, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')
    # view_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    is_subscription = models.BooleanField(default=True, verbose_name='Подписка')

    def __str__(self):
        return f'{self.title} - {self.content}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
