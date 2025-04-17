from core.models import SiteSettings


def core_func(request):
    site_settings = SiteSettings.objects.first()

    return {
        'site_settings': site_settings,
    }