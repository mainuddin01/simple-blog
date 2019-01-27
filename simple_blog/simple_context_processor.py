from site_settings.models import Setting

site_data = Setting.objects.first()

def simple_context(request):
    return {
        'site_data': site_data,
    }