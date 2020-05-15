from django import forms
from django.core.validators import validate_email


class CheckoutForm(forms.Form):
    first_name = forms.CharField(label='Имя', max_length=30, required=True)
    last_name = forms.CharField(label='Фамилия', max_length=30, required=True)
    email = forms.CharField(label='E-mail', max_length=255, required=True, validators=[validate_email])
    comment = forms.CharField(label='Комментарий', widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super(CheckoutForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
            field.help_text = ''
            field.label = False
