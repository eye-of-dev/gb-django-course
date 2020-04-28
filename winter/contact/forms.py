from django import forms

from contact.models import Feedback
from django.forms import ModelForm


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'subject', 'description')

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
            field.help_text = ''
            field.label = False
