from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy


class AdminPermissionMixin(PermissionRequiredMixin):
    permission_required = ('is_staff', 'is_superuser')
    login_url = reverse_lazy('admin_panel:login_admin')
