from django.urls import path

from users_app.apps import UsersAppConfig
from users_app.views import LoginView, LogoutView, RegisterView

app_name = UsersAppConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register')
]
