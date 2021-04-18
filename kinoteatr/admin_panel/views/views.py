from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

from admin_panel.views.permission_mixin import AdminPermissionMixin
from admin_panel.forms.authentication_form import LoginForm


class IndexAdmin(AdminPermissionMixin, View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)


class LoginUserAdmin(LoginView):
    authentication_form = LoginForm
    template_name = 'registration/login.html'
    redirect_authenticated_user = True


class LogoutAdmin(View):
    def get(self, request):
        logout(request)
        return redirect('admin_panel:login_admin')
