from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

from admin_panel.views.permission_mixin import AdminPermissionMixin
from admin_panel.forms.authentication_form import LoginForm

from admin_panel.services.statistics import Statistic


class IndexAdmin(AdminPermissionMixin, View):
    template_name = 'index.html'

    def get(self, request):
        statistics = Statistic()

        man, woman = statistics.get_gender()
        context = {
            'movie_count': statistics.get_movies(),
            'user_count': statistics.get_users(),
            'last_movies': statistics.get_last_10_movies(),
            'genre': statistics.get_genre(),
            'session': statistics.get_session(),
            'man': man,
            'woman': woman,
            'load': statistics.get_network_load()
        }

        return render(request, self.template_name, context)


class LoginUserAdmin(LoginView):
    authentication_form = LoginForm
    template_name = 'registration/login.html'


class LogoutAdmin(View):
    def get(self, request):
        logout(request)
        return redirect('admin_panel:login_admin')
