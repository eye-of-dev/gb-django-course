from django.core.management import call_command
from django.test import TestCase, Client


class TestAuthapp(TestCase):
    def setUp(self):
        call_command('flush', '--noinput')
        call_command('loaddata', 'test_db.json')
        self.client = Client()

    def test_authapp_urls(self):
        response = self.client.get('/auth/login/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/auth/registration/')
        self.assertEqual(response.status_code, 200)

    def test_user_login(self):
        # главная без логина
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_anonymous)
        self.assertEqual(response.context['title'], 'главная')
        self.assertNotContains(response, 'Пользователь', status_code=200)
        # self.assertNotIn('Пользователь', response.content.decode())

        # данные пользователя
        self.client.login(username='django', password='geekbrains')

        # логинимся
        response = self.client.get('/auth/login/')
        self.assertFalse(response.context['user'].is_anonymous)
        self.assertEqual(response.context['user'], self.user)

        # главная после логина
        response = self.client.get('/')
        self.assertContains(response, 'Пользователь', status_code=200)
        self.assertEqual(response.context['user'], self.user)
