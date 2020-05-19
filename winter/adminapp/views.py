from django.contrib.auth.decorators import user_passes_test
from django.core.serializers import serialize
from django.db import transaction
from django.forms import inlineformset_factory
from django.http import JsonResponse

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from authapp.models import ShopUser

from orderapp.models import Orders, OrdersUserInfo, OrdersProducts
from orderapp.forms import OrdersForm, OrdersProductsForm
from shop.models import ProductCategories, Products


class OrdersListView(ListView):
    model = Orders
    context_object_name = 'orders'
    ordering = '-pk'
    paginate_by = 5

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(OrdersListView, self).get_context_data(**kwargs)
        context['title'] = 'Список заказов'
        return context


class OrdersReadView(DetailView):
    model = Orders

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(OrdersReadView, self).get_context_data(**kwargs)
        context['title'] = f'Просмотр заказа: {self.object.pk}'
        return context


class OrdersUpdateView(UpdateView):
    model = Orders
    fields = ['total', 'status']
    success_url = reverse_lazy('admin:orders_list')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(OrdersUpdateView, self).get_context_data(**kwargs)
        context['title'] = f'Обновление заказа: {self.object.pk}'
        OrderFormSet = inlineformset_factory(Orders, OrdersProducts, form=OrdersProductsForm, extra=1)
        if self.request.POST:
            context['order_products'] = OrderFormSet(self.request.POST, instance=self.object)
        else:
            context['order_products'] = OrderFormSet(instance=self.object)

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        order_products = context['order_products']

        with transaction.atomic():
            self.object = form.save()
            if order_products.is_valid():
                order_products.instance = self.object
                order_products.save()

        return super(OrdersUpdateView, self).form_valid(form)


class OrdersDeleteView(DeleteView):
    model = Orders
    success_url = reverse_lazy('admin:orders_list')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


class ProductsCategoriesListView(ListView):
    model = ProductCategories
    template_name = 'product_categories/list.html'
    context_object_name = 'categories'
    ordering = '-pk'
    paginate_by = 5

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductsCategoriesListView, self).get_context_data(**kwargs)
        context['title'] = 'Список категорий'
        return context


class ProductsCategoriesCreateView(CreateView):
    model = ProductCategories
    template_name = 'product_categories/create.html'
    success_url = reverse_lazy('admin:product_categories_index')
    fields = '__all__'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductsCategoriesCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Создание категории'
        return context


class ProductsCategoriesReadView(DetailView):
    model = ProductCategories
    template_name = 'product_categories/read.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductsCategoriesReadView, self).get_context_data(**kwargs)
        context['title'] = 'Просмотр категории: ' + self.object.title
        return context


class ProductsCategoriesUpdateView(UpdateView):
    model = ProductCategories
    template_name = 'product_categories/update.html'
    success_url = reverse_lazy('admin:product_categories_index')
    fields = '__all__'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductsCategoriesUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Обновление категории: ' + self.object.title
        return context


class ProductsCategoriesDeleteView(DeleteView):
    model = ProductCategories
    success_url = reverse_lazy('admin:product_categories_index')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


class ProductsListView(ListView):
    model = Products
    template_name = 'products/list.html'
    context_object_name = 'products'
    ordering = '-pk'
    paginate_by = 5

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context['title'] = 'Список продуктов'
        return context


class ProductsCreateView(CreateView):
    model = Products
    template_name = 'products/create.html'
    success_url = reverse_lazy('admin:products_list')
    fields = '__all__'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductsCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Создание продукта'
        return context


class ProductsReadView(DetailView):
    model = Products
    template_name = 'products/read.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductsReadView, self).get_context_data(**kwargs)
        context['title'] = 'Просмотр продукта: ' + self.object.title
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.is_ajax():
            return JsonResponse({
                'pk': self.object.pk,
                'price': self.object.price
            })
        else:
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)


class ProductsUpdateView(UpdateView):
    model = Products
    template_name = 'products/update.html'
    success_url = reverse_lazy('admin:products_list')
    fields = '__all__'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductsUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Обновление продукта: ' + self.object.title
        return context


class ProductsDeleteView(DeleteView):
    model = Products
    success_url = reverse_lazy('admin:products_list')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


class UsersListView(ListView):
    model = ShopUser
    template_name = 'users/list.html'
    context_object_name = 'users'
    ordering = '-pk'
    paginate_by = 5

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UsersListView, self).get_context_data(**kwargs)
        context['title'] = 'Список пользователей'
        return context


class UsersCreateView(CreateView):
    model = ShopUser
    template_name = 'users/create.html'
    success_url = reverse_lazy('admin:users_list')
    fields = '__all__'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UsersCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Создание пользователя'
        return context


class UsersReadView(DetailView):
    model = ShopUser
    template_name = 'users/read.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UsersReadView, self).get_context_data(**kwargs)
        context['title'] = 'Просмотр пользователя: ' + self.object.username
        return context


class UsersUpdateView(UpdateView):
    model = ShopUser
    template_name = 'users/update.html'
    success_url = reverse_lazy('admin:users_list')
    fields = '__all__'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UsersUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Обновление пользователя: ' + self.object.username
        return context


class UsersDeleteView(DeleteView):
    model = ShopUser
    success_url = reverse_lazy('admin:users_list')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
