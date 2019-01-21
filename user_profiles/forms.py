from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile


class UserCreateForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = UserProfile
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'profile_image', 'biography')

class UserEditForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = UserProfile
        fields = ('first_name', 'last_name', 'email', 'profile_image', 'biography')
