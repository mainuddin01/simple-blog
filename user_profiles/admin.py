from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreateForm, UserEditForm
from .models import UserProfile

# Register your models here.
class UserProfileAdmin(UserAdmin):
    model = UserProfile
    add_form = UserCreateForm
    form = UserEditForm

admin.site.register(UserProfile, UserProfileAdmin)