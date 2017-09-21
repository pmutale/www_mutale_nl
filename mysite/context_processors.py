from django.conf import settings
from django.http.response import HttpResponse


def google_analytics(request):
    """
    Google analytics intergration
    :param request:
    :return:
    """
    ga_prop_id = getattr(settings.GOOGLE_ANALYTICS_DOMAIN, 'GOOGLE_ANALYTICS_PROPERTY_ID', False)

    if not settings.DEBUG:
        return {
            'GOOGLE_ANALYTICS_PROPERTY_ID': ga_prop_id,
        }
    else:
        return {
            'GOOGLE_ANALYTICS_PROPERTY_ID': 0,
        }
