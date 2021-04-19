from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic import View
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from admin_panel.forms.user_form import UserForm
from admin_panel.views.permission_mixin import AdminPermissionMixin

User = get_user_model()


class ListUser(AdminPermissionMixin, ListView):
    model = User
    template_name = 'user/list_user.html'
    paginate_by = 10
    context_object_name = 'users'


class EditUser(AdminPermissionMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'user/edit_user.html'
    success_url = reverse_lazy('admin_panel:list_users_admin')
    context_object_name = 'form'


class DeleteUser(AdminPermissionMixin, View):
    model = User
    redirect_url = 'admin_panel:list_users_admin'

    def get(self, request, pk):
        user = get_object_or_404(self.model, pk=pk)
        user.delete()
        return redirect(self.redirect_url)
