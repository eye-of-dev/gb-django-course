from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from shop.models import ProductCategories

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


def product_categories_delete(request, pk):
    category = get_object_or_404(ProductCategories, pk=pk)
    category.delete()
    return redirect('adminapp:product_categories_index')
