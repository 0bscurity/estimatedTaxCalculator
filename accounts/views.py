from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView
from django.contrib.auth import login
from django.urls import reverse_lazy

from accounts.forms import RegistrationForm


class Login(LoginView):
    template_name = 'accounts/login.html'
    next_page = 'home'


class Logout(LogoutView):
    next_page = 'home'


class RegistrationView(FormView):
    template_name = 'accounts/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)