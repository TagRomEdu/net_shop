from django.contrib.auth.forms import UserCreationForm

from users_app.models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
