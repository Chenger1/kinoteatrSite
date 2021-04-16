from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from cinema.models.page import Contact

from admin_panel.forms.contacts_form import ContactsForm
from admin_panel.forms.seo_form import SeoForm


class ListContacts(ListView):
    template_name = 'contacts/list_contacts.html'
    model = Contact
    context_object_name = 'contacts'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListContacts, self).get_context_data(**kwargs)
        context['seo'] = self.model.objects.filter(top_seo=True).first().seo
        return context


class UpdateContactInfo(UpdateView):
    model = Contact
    form_class = ContactsForm
    context_object_name = 'form'
    template_name = 'contacts/edit_contact.html'
    success_url = reverse_lazy('admin_panel:list_contacts_admin')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['seo_form'] = SeoForm(self.request.POST,
                                          instance=self.object.seo)
        else:
            context['seo_form'] = SeoForm(instance=self.object.seo)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        seo_form = context['seo_form']
        self.object = form.save()
        if seo_form.is_valid():
            self.object.seo = seo_form.save()
        else:
            return super().form_invalid(form)
        return super().form_valid(form)
