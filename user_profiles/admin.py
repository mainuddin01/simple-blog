from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreateForm, UserEditForm
from .models import UserProfile, UserSocialLink

# Register your models here.
class UserProfileAdmin(UserAdmin):
    model = UserProfile
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'profile_image', 'biography')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_form = UserCreateForm
    form = UserEditForm

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserSocialLink)