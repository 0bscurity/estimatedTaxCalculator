from django.contrib.auth.views import LoginView


class Login(LoginView):
    template_name = 'accounts/login.html'
