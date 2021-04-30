from django.views.generic.detail import DetailView
from django.views.generic import View
from django.contrib.auth import logout
from django.shortcuts import redirect

from cinema.models.user import User
from cinema.models.banners import OnTopBanner, BackgroundImage
from cinema.models.page import MainPage

from cinema.services.get_banners import get_context_for_generic_views


class UserDetail(DetailView):
    model = User
    template_name = 'user/profile.html'
    pages = [OnTopBanner, BackgroundImage, MainPage]
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context_for_generic_views(self.pages))
        return context


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('cinema:main_page')
