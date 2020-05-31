from django.http import JsonResponse
from shop.models import ProductCategories

from shop.models import Products

from mainpage.views import CommonClass, DetailClass

from mainpage.views import ListClass


class CatalogView(ListClass):
    model = Products
    template_name = 'catalog.html'
    title = 'каталог'
    context_object_name = 'list_products'

    @staticmethod
    def get_list_categories():
        return ProductCategories.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CatalogView, self).get_context_data(**kwargs)
        context['list_categories'] = self.get_list_categories()
        return context


class JSONResponseMixin:
    """
    A mixin that can be used to render a JSON response.
    """

    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(
            self.get_data(context),
            **response_kwargs
        )

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return context


class CategoryView(JSONResponseMixin, DetailClass):
    template_name = 'category.html'
    model = ProductCategories
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['list_categories'] = CatalogView().get_list_categories()
        return context


class ProductView(DetailClass):
    template_name = 'product.html'
    model = Products
    context_object_name = 'product'

    def get_similar_products(self):
        return Products.objects.filter(category=self.object.category.id).exclude(pk=self.object.id).all()

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['category'] = self.object.category
        context['similar_products'] = self.get_similar_products()
        return context
