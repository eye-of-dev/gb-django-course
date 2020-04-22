from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404

from cabinetapp.forms import ShopUserProfileForm
from django.urls import reverse
from django.utils.decorators import method_decorator

from shop.models import Products

from cabinetapp.models import WishList

from mainpage.views import ListClass


@login_required()
def profile_view(request):
    """
    Обновление личных данных(профиля) на сайте
    :param request:
    :return:
    """
    if request.method == 'POST':
        change_form = ShopUserProfileForm(request.POST, request.FILES, instance=request.user)
        if change_form.is_valid():
            change_form.save()
            return redirect('cabinetapp:profile')
    else:
        change_form = ShopUserProfileForm(instance=request.user)

    content = {
        'title': 'редактирование профиля',
        'change_form': change_form
    }
    return render(request, 'profile.html', content)


class WishlistView(ListClass):
    model = WishList
    template_name = 'wishlist.html'
    title = 'Список желаний'
    context_object_name = 'wish_list'

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(WishlistView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return WishList.objects.filter(user=self.request.user)


@login_required()
def wishlist_add(request, pk):
    """
    Функция добавления продукта в списоок желаний
    :param request:
    :param pk:
    :return:
    """
    product = get_object_or_404(Products, pk=pk)

    try:
        WishList(user=request.user, product=product).save()
    except IntegrityError:
        # TODO:  Сделать сообщение пользователю, что он уже добавил продукт в список желаний
        pass

    if 'login' in request.META.get('HTTP_REFERER'):
        return redirect(reverse('shop:product_view', args=[pk]))

    return redirect(request.META.get('HTTP_REFERER'))


@login_required()
def wishlist_delete(request, pk):
    """
    Удаление товаров из списка желаний
    :param request:
    :param wpk:
    :return:
    """
    product = get_object_or_404(WishList, pk=pk)
    product.delete()
    return redirect(request.META.get('HTTP_REFERER'))
