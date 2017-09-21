from django.conf import settings
from django.http.response import HttpResponse


def google_analytics(request):
    """
    Google analytics intergration
    :param request:
    :return:
    """
    ga_prop_id = getattr(settings, 'GOOGLE_ANALYTICS_PROPERTY_ID', False)
    ga_domain = getattr(settings, 'GOOGLE_ANALYTICS_DOMAIN', False)

    response = HttpResponse()

    if response.status_code in [500, 400]:
        stop = True

        if not settings.DEBUG and ga_prop_id and stop:
            return {
                'GOOGLE_ANALYTICS_PROPERTY_ID': ga_prop_id,
                'GOOGLE_ANALYTICS_DOMAIN': ga_domain
            }
        elif settings.DEBUG:
            return {
                'GOOGLE_ANALYTICS_PROPERTY_ID': 'development',
                'GOOGLE_ANALYTICS_DOMAIN': 'auto'
            }
