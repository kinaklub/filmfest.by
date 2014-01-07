from django import template
from django.conf import settings

register = template.Library()

PIWIK_ENABLED = getattr(settings, 'PIWIK_ENABLED', False)
PIWIK_URL = getattr(settings, 'PIWIK_URL', 'stat.garage22.net')
PIWIK_SITE_ID = getattr(settings, 'PIWIK_SITE_ID', '9')


@register.inclusion_tag('cpm_common/tags/piwik.html')
def piwik():
    return {
        'piwik_enabled': PIWIK_ENABLED,
        'piwik_url': PIWIK_URL,
        'piwik_site_id': PIWIK_SITE_ID,
    }
