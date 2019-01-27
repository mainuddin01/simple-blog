from django.contrib import admin

from .models import Setting

# Register your models here.
class SettingAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count():
            return False
        return True


admin.site.register(Setting, SettingAdmin)
