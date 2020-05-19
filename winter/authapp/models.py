from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.timezone import now

import winter.settings


class ShopUser(AbstractUser):
    avatar = models.ImageField('Аватар', upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField('Возраст', default=18)
    activation_key = models.CharField('Ключ активации', max_length=128, blank=True)
    activation_key_expires = models.DateTimeField('Время жизни ключа', default=(now() + timedelta(hours=48)))

    @property
    def user_name(self):
        return f'{self.first_name} {self.last_name} - ({self.email})'

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


class ShopUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'M'),
        (FEMALE, 'W')
    )

    LANG_RU = 'ru'
    LANG_EN = 'en'

    LANG_CHOICES = (
        (LANG_RU, 'RU'),
        (LANG_EN, 'EN')
    )

    user = models.OneToOneField(ShopUser, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    about = models.TextField('О себе', max_length=512, blank=True)
    gender = models.CharField('Пол', max_length=1, choices=GENDER_CHOICES, blank=True)
    locale = models.CharField('Язык', max_length=2, choices=LANG_CHOICES, blank=True)
    link = models.CharField('Адрес страницы', max_length=255, blank=True)

    @receiver(post_save, sender=ShopUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ShopUserProfile.objects.create(user=instance)

    @receiver(post_save, sender=ShopUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.shopuserprofile.save()
