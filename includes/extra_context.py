from django.conf import settings

def general_context(request):
    """
    Returns common context stuff for use in HTML templates.
    """
    return {
        'YUI_URL': settings.YUI_URL,
    }
