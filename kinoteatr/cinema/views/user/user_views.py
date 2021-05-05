from django.views.generic.detail import DetailView
from django.views.generic import View
from django.contrib.auth import logout, get_user_model
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from cinema.models.session import Ticket

from cinema.forms.user_form import LoginForm, RegistrationForm

from cinema.services.get_banners import get_context_for_generic_views

User = get_user_model()


class UserDetail(DetailView):
    model = User
    template_name = 'user/profile.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context_for_generic_views())
        context['tickets'] = self.object.tickets.all()
        return context


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('cinema:main_page')


class LoginUser(LoginView):
    authentication_form = LoginForm
    template_name = 'user/login.html'

    def get_success_url(self):
        return reverse('cinema:main_page')


class RegistrationView(View):
    template_name = 'user/registration.html'
    form = RegistrationForm

    def get(self, request):
        form = self.form()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            login_user = authenticate(username=form.cleaned_data.get('email'), password=form.cleaned_data.get('password2'))
            if login_user:
                login(request, login_user)
            return redirect('cinema:main_page')
        else:
            return render(request, self.template_name, {'form': form})


class RevertTicket(View):
    model = Ticket

    def get(self, request, pk):
        ticket = get_object_or_404(self.model, pk=pk)
        if ticket in request.user.tickets.all():
            ticket.delete()
        return redirect('cinema:user_profile', pk=request.user.pk)
