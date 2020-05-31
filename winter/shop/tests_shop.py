from django.test import TestCase

from shop.models import ProductCategories, Products


class ProductsTestCase(TestCase):
    def setUp(self):
        category = ProductCategories.objects.create(title="стулья")
        self.product = Products.objects.create(category=category,
                                               title="стул 1",
                                               price=1999.5,
                                               quantity=150)

    def test_product_get(self):
        product = Products.objects.get(title="стул 1")
        self.assertEqual(product, self.product)

    def test_product_print(self):
        product = Products.objects.get(title="стул 1")
        self.assertEqual(str(product), 'стул 1')
