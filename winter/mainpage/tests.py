from django.core.management import call_command
from django.test import TestCase, Client


class TestMainpage(TestCase):
    def setUp(self):
        call_command('flush', '--noinput')
        call_command('loaddata', 'test_db.json')
        self.client = Client()

    def test_mainpage_urls(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

