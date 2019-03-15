from django.db import models
from django.utils import timezone


class Subscriber(models.Model):
    email = models.EmailField(max_length=128, verbose_name='Емейл')
    name = models.CharField(max_length=128, verbose_name='Имя')
    message = models.TextField(blank=True, null=True, default=None, max_length=128, verbose_name='Сообщение')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата обращения')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата редактирования обращения')

    def __str__(self):
        return "Пользователь %s %s" % (self.name, self.email)

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'