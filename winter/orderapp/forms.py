from django import forms

from orderapp.models import Orders, OrdersProducts


class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(OrdersForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class OrdersProductsForm(forms.ModelForm):
    class Meta:
        model = OrdersProducts
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(OrdersProductsForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
