"""
    Contact app
"""
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from mainpage.views import TemplateClass

from contact.forms import FeedbackForm


class ContactView(FormView, TemplateClass):
    form_class = FeedbackForm
    template_name = 'contact.html'
    success_url = reverse_lazy('contact:index')

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['title'] = 'контакты'
        return context

    def form_valid(self, form):
        form_class = self.form_class(self.request.POST)
        form_class.save()
        return redirect(self.success_url)
