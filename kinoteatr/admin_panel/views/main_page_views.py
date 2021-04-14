from django.views.generic.edit import UpdateView

from cinema.models.page import MainPage

from admin_panel.forms.main_page_form import MainPageForm
from admin_panel.forms.seo_form import SeoForm


class EditMainPage(UpdateView):
    model = MainPage
    template_name = 'main_page/edit_main_page.html'
    context_object_name = 'form'
    form_class = MainPageForm

    def get_object(self, queryset=None):
        return self.model.load()

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['seo_form'] = SeoForm(self.request.POST, instance=self.object.seo)
        else:
            data['seo_form'] = SeoForm(instance=self.object.seo)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        seo_form = context['seo_form']
        self.object = form.save()
        if seo_form.is_valid():
            self.object.seo = seo_form.save()
        else:
            return super().form_invalid(form)
        return super().form_valid(form)
