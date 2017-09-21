from django.conf import settings


def google_analytics(request):
    """
    Google analytics intergration
    :param request:
    :return:
    """
    ga_prop_id = settings.GOOGLE_ANALYTICS_PROPERTY_ID

    if not settings.DEBUG:
        return {
            'GOOGLE_TICS_PPT_ID': ga_prop_id,
        }
    else:
        return {
            'GOOGLE_TICS_PPT_ID': 0,
        }
