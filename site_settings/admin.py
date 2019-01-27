from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Setting

# Register your models here.
class SettingAdmin(SummernoteModelAdmin):
    summernote_fields = ('header_ad', 'middle_ad', 'footer_ad', 'sidebar_ad')

    def has_add_permission(self, request):
        if self.model.objects.count():
            return False
        return True


admin.site.register(Setting, SettingAdmin)
