from django.shortcuts import get_object_or_404, redirect
from django.db import transaction
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import View

from admin_panel.forms.seo_form import SeoForm
from admin_panel.views.permission_mixin import AdminPermissionMixin


class AddPageMixin(AdminPermissionMixin, CreateView):
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


class UpdatePageMixin(AdminPermissionMixin, UpdateView):
    model = None
    form_class = None
    inline_form_set = None
    template_name = None
    context_object_name = 'form'
    success_url = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = self.inline_form_set(self.request.POST,
                                                      self.request.FILES,
                                                      instance=self.object)
            context['formset'].full_clean()
            context['seo_form'] = SeoForm(self.request.POST,
                                          instance=self.object.seo)
        else:
            context['formset'] = self.inline_form_set(instance=self.object)
            context['seo_form'] = SeoForm(instance=self.object.seo)
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset = context['formset']
        seo_form = context['seo_form']
        response = super().form_valid(form)
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
        return response


class DeleteMixin(AdminPermissionMixin, View):
    model = None
    redirect_url = None

    def get(self, request, pk):
        inst = get_object_or_404(self.model, pk=pk)
        seo = inst.seo
        if seo:
            seo.delete()
        inst.delete()
        return redirect(self.redirect_url)


class DeleteGalleryImageMixin(AdminPermissionMixin, View):
    model = None
    redirect_url = None

    def get(self, request, pk):
        inst = get_object_or_404(self.model, pk=pk)
        inst_pk = inst.entity.pk
        inst.delete()
        return redirect(self.redirect_url, pk=inst_pk)
