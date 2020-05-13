from django.db import transaction
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from mainpage.views import TemplateClass

from checkoutapp.forms import CheckoutForm

from orderapp.models import Order, OrderUserInfo, OrderProducts

from cartapp.models import CartCommon


class CheckoutClass(FormView):
    template_name = 'checkout.html'
    form_class = CheckoutForm
    success_url = reverse_lazy('checkoutapp:success')

    def get_context_data(self, **kwargs):
        context = super(CheckoutClass, self).get_context_data(**kwargs)
        context['title'] = 'оформление заказа'
        return context

    def form_valid(self, form):
        cart = CartCommon(self.request.COOKIES.get('cart_uuid'))

        with transaction.atomic():
            # так себе код, лучше написать не хватает знаний и опыта
            order = Order(total=cart.total_cart_price_products, comment=self.request.POST['comment'])
            order.save()
            order.orderuserinfo.first_name = self.request.POST['first_name']
            order.orderuserinfo.last_name = self.request.POST['last_name']
            order.orderuserinfo.email = self.request.POST['email']
            order.save()

            for model in cart.get_user_products():
                order_product = OrderProducts(order=order, product=model.product)
                order_product.quantity = model.quantity
                order_product.price = model.price
                order_product.save()

                model.delete()

        return redirect(self.success_url)

    def get_initial(self):
        form = super(CheckoutClass, self).get_initial()
        if self.request.user.is_authenticated:
            form.update({'first_name': self.request.user.first_name, 'last_name': self.request.user.last_name,
                         'email': self.request.user.email})

        return form


class CheckoutSuccessClass(TemplateClass):
    template_name = 'success.html'
    title = 'оформление заказа'
