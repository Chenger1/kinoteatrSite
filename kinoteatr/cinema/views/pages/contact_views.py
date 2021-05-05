from django.views.generic.list import ListView

from cinema.services.get_banners import get_context_for_generic_views
from cinema.models.page import Contact


class DisplayContactPage(ListView):
    model = Contact
    template_name = 'pages/contacts.html'
    context_object_name = 'contacts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context_for_generic_views())
        return context
