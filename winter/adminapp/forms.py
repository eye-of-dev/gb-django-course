from django import forms
from shop.models import ProductCategories


class ProductCategoryEditForm(forms.ModelForm):
    discount = forms.IntegerField(label='скидка', required=False, min_value=0, max_value=90, initial=0)

    class Meta:
        model = ProductCategories
        exclude = ()
