from django.db import models


class Feedback(models.Model):
    name = models.CharField('Имя', max_length=64)
    email = models.CharField('E-mail', max_length=128)
    subject = models.CharField('Тема письма', max_length=128)
    description = models.TextField('Текст письма')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"

    def __str__(self):
        return self.title
