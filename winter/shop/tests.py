from django.core.management import call_command
from django.test import TestCase, Client


class TestShop(TestCase):
    def setUp(self):
        call_command('flush', '--noinput')
        call_command('loaddata', 'test_db.json')
        self.client = Client()

    def test_shop_urls(self):
        response = self.client.get('/shop/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/shop/category/2')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/shop/product/8')
        self.assertEqual(response.status_code, 200)

