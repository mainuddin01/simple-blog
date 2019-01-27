from django.contrib import admin
<<<<<<< HEAD
from django_summernote.admin import SummernoteModelAdmin
=======
>>>>>>> 4a6b0a9c21d0bd3fb8449b633fa78f51882603fc

from .models import Setting

# Register your models here.
<<<<<<< HEAD
class SettingAdmin(SummernoteModelAdmin):
    summernote_fields = ('header_ad', 'middle_ad', 'footer_ad', 'sidebar_ad')

=======
class SettingAdmin(admin.ModelAdmin):
>>>>>>> 4a6b0a9c21d0bd3fb8449b633fa78f51882603fc
    def has_add_permission(self, request):
        if self.model.objects.count():
            return False
        return True


admin.site.register(Setting, SettingAdmin)
