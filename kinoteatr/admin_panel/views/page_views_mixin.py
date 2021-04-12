from django.db import transaction
from django.views.generic.edit import CreateView

from admin_panel.forms.seo_form import SeoForm


class AddPageMixin(CreateView):
    model = None
    form_class = None
    inline_form_set = None
    template_name = None
    context_object_name = 'form'
    success_url = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = self.inline_form_set(self.request.POST, self.request.FILES)
            data['seo_form'] = SeoForm(self.request.POST)
        else:
            data['formset'] = self.inline_form_set()
            data['seo_form'] = SeoForm()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        seo_form = context['seo_form']
        self.object = form.save()
        with transaction.atomic():
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
            else:
                return super().form_invalid(form)
            if seo_form.is_valid():
                self.object.seo = seo_form.save()
            else:
                return super().form_invalid(form)
        return super().form_valid(form)
