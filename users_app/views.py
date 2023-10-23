from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView


class LoginView(BaseLoginView):
    template_name = 'users_app/login.html'


class LogoutView(BaseLogoutView):
    pass
