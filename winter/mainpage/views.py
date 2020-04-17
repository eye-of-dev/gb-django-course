"""
    Mainpage app
"""
import uuid

from django.views.generic import TemplateView, DetailView

from cartapp.models import CartCommon


class CommonClass:
    """
    Служебный класс в котором приписаны
    общие методы для всего приложения
    """

    def get(self, request, *args, **kwargs):
        cart_uuid = request.COOKIES.get('cart_uuid')
        if cart_uuid is None:
            cart_uuid = uuid.uuid1()

        response = super(CommonClass, self).get(request, *args, **kwargs)
        response.set_cookie('cart_uuid', value=cart_uuid, max_age=30 * 24 * 60 * 60)
        return response

    def cart(self):
        return CartCommon(self.request.COOKIES.get('cart_uuid'))


class TemplateClass(CommonClass, TemplateView):
    title = None

    def get_context_data(self, **kwargs):
        context = super(TemplateClass, self).get_context_data(**kwargs)
        context['cart'] = self.cart()
        context['title'] = self.title
        return context


class DetailClass(CommonClass, DetailView):
    def get_context_data(self, **kwargs):
        context = super(DetailClass, self).get_context_data(**kwargs)
        context['cart'] = self.cart()
        context['title'] = self.object.title
        return context


class Mainpage(TemplateClass):
    template_name = 'index.html'
    title = 'главная'
