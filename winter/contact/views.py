"""
    Contact app
"""
from mainpage.views import TemplateClass


class ContactView(TemplateClass):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['title'] = 'контакты'
        return context
