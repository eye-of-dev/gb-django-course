from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, transaction
from django.shortcuts import render, redirect, get_object_or_404

from cabinetapp.forms import ShopUserEditForm, ShopUserProfileEditForm
from django.urls import reverse
from django.utils.decorators import method_decorator

from shop.models import Products

from cabinetapp.models import WishList

from mainpage.views import ListClass


@login_required()
@transaction.atomic
def profile_view(request):
    """
    Обновление личных данных(профиля) на сайте
    :param request:
    :return:
    """
    if request.method == 'POST':
        user_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        profile_form = ShopUserProfileEditForm(request.POST, instance=request.user.shopuserprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('cabinetapp:profile')
    else:
        user_form = ShopUserEditForm(instance=request.user)
        profile_form = ShopUserProfileEditForm(instance=request.user.shopuserprofile)

    content = {
        'title': 'редактирование профиля',
        'user_form': user_form,
        'profile_form': profile_form
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
