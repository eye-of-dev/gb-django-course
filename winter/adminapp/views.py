from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from shop.models import ProductCategories, Products

from adminapp.forms import ProductCategoriesAdminForm


@user_passes_test(lambda u: u.is_superuser)
def product_categories_index(request):
    categories_list = ProductCategories.objects.all()

    content = {
        'categories_list': categories_list,
        'title': 'категории'
    }

    return render(request, 'product_categories/categories_list.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_categories_create(request):
    form = ProductCategoriesAdminForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('adminapp:product_categories_index')

    content = {
        'form': form,
        'title': 'создание категории'
    }

    return render(request, 'product_categories/create.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_categories_read(request, pk):
    category = get_object_or_404(ProductCategories, pk=pk)

    content = {
        'category': category,
        'title': 'просмотр категории: ' + category.title
    }

    return render(request, 'product_categories/read.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_categories_update(request, pk):
    category = get_object_or_404(ProductCategories, pk=pk)
    if request.method == 'POST':
        form = ProductCategoriesAdminForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('adminapp:product_categories_index')

    form = ProductCategoriesAdminForm(instance=category)

    content = {
        'category': category,
        'form': form,
        'title': 'редактирование категории: ' + category.title
    }

    return render(request, 'product_categories/update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_categories_delete(request, pk):
    category = get_object_or_404(ProductCategories, pk=pk)
    category.delete()
    return redirect('adminapp:product_categories_index')


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
