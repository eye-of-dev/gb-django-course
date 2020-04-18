"""
    Shop app
"""
from shop.models import ProductCategories

from shop.models import Products

from mainpage.views import CommonClass, DetailClass

from mainpage.views import ListClass


class CatalogView(ListClass):
    model = Products
    template_name = 'category.html'
    title = 'каталог'
    context_object_name = 'list_products'

    @staticmethod
    def get_list_categories():
        return ProductCategories.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CatalogView, self).get_context_data(**kwargs)
        context['list_categories'] = self.get_list_categories()
        return context


class CategoryView(DetailClass):
    template_name = 'category.html'
    model = ProductCategories

    def get_list_products(self):
        return Products.objects.filter(category=self.object.id).all()

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['list_categories'] = CatalogView().get_list_categories()
        context['list_products'] = self.get_list_products()
        return context


class ProductView(DetailClass):
    template_name = 'product.html'
    model = Products

    def get_similar_products(self):
        return Products.objects.filter(category=self.object.category.id).exclude(pk=self.object.id).all()

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['category'] = self.object.category
        context['similar_products'] = self.get_similar_products()
        return context
