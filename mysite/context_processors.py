from django.conf import settings


def google_analytics(request):
    """
    Google analytics intergration
    :param request:
    :return:
    """
    ga_prop_id = getattr(settings, 'GOOGLE_ANALYTICS_PROPERTY_ID', False)
    ga_domain = getattr(settings, 'GOOGLE_ANALYTICS_DOMAIN', False)

    state = True

    if not settings.DEBUG and ga_prop_id and ga_domain:
        return {
            'GOOGLE_ANALYTICS_PROPERTY_ID': ga_prop_id if state else '',
            'GOOGLE_ANALYTICS_DOMAIN': ga_domain if state else ''
        }
    elif settings.DEBUG:
        return {
            'GOOGLE_ANALYTICS_PROPERTY_ID': 'development',
            'GOOGLE_ANALYTICS_DOMAIN': 'auto'
        }
