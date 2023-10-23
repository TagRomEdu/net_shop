from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users_app.forms import UserForm, CustomAuthForm
from users_app.models import User


class LoginView(BaseLoginView):
    model = User
    form_class = CustomAuthForm
    template_name = 'users_app/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('catalog:main')
    template_name = 'users_app/register.html'
