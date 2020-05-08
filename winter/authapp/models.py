from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse
from django.utils.timezone import now

import winter.settings


class ShopUser(AbstractUser):
    avatar = models.ImageField('Аватар', upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField('Возраст', default=18)
    activation_key = models.CharField('Ключ активации', max_length=128, blank=True)
    activation_key_expires = models.DateTimeField('Время жизни ключа', default=(now() + timedelta(hours=48)))

    @property
    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        return True

    def send_verify_mail(self):
        verify_link = reverse('authapp:confirm_activation', args=[self.activation_key])

        title = f'Подтверждение учетной записи {self.username}'
        message = f'Для подтверждения учетной записи {self.username} ' \
                  f'на портале {winter.settings.DOMAIN_NAME} пройдите по ссылке ' \
                  f'{winter.settings.DOMAIN_NAME}{verify_link}'

        return send_mail(title, message, winter.settings.EMAIL_HOST_USER, [self.email], fail_silently=False)
