from django import template
from django.conf import settings
from django.utils import translation


register = template.Library()


@register.inclusion_tag('cpm/tags/timetable.html')
def cpm_timetable():
    language = translation.get_language().split('-')[0]
    language = language or 'en'
    next_url = 'http://cpm.filmfest.by/%s/timetable/' % language
    return {
        'next_url': next_url,
        'STATIC_URL': settings.STATIC_URL,
    }


@register.inclusion_tag('cpm/tags/manifest.html')
def cpm_manifest():
    language = translation.get_language().split('-')[0]
    language = language or 'en'
    return {
        'language': language,
    }


@register.inclusion_tag('cpm/tags/banners_list.html')
def banners_list(banners):
    return {'banners': banners}
