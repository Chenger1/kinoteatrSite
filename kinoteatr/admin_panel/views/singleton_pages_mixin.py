from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View

from admin_panel.views.page_views_mixin import UpdatePageMixin


class EditSingletonMixin(UpdatePageMixin):
    def get_object(self, queryset=None):
        return self.model.load()


class DeleteSingletonGalleryImageMixin(View):
    model = None
    redirect_url = None

    def get(self, request, pk):
        inst = get_object_or_404(self.model, pk=pk)
        inst.delete()
        return redirect(self.redirect_url)
