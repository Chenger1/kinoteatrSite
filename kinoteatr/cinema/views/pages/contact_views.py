from django.views.generic.list import ListView

from cinema.services.get_banners import get_context_for_generic_views
from cinema.models.page import Contact


class DisplayContactPage(ListView):
    model = Contact
    template_name = 'pages/contacts.html'
    context_object_name = 'contacts'

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.filter(status=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context_for_generic_views())
        main_contact_seo = self.model.objects.filter(top_seo=True).first()
        if main_contact_seo:
            context['seo'] = main_contact_seo.seo
        return context
