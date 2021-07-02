import datetime
from django.db import models
from django.forms import EmailField, EmailInput, TextInput, Textarea
from django.utils import timezone


class Email(models.Model):
    from_email = models.EmailField('Получатель')
    subject = models.CharField('Тема', max_length=200)
    message = models.TextField('Текст сообщения')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Sort(models.Model):
    status = models.BooleanField('status')

    def __str__(self):
        return self.status