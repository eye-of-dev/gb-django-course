from django import forms

# Create your models here.
from shop.models import ProductCategories


class ProductCategoriesAdminForm(forms.ModelForm):
    class Meta:
        model = ProductCategories
        fields = '__all__'
