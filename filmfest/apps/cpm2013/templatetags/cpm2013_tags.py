from django import template
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils import translation
from django.conf import settings


register = template.Library()


MAINMENU_ITEMS = [
    (_('Home'), reverse('cpm2013:index')),
    (_('Rules'), reverse('cpm2013:rules')),
    (_('Submit your film!'), reverse('cpm2013:submit')),
]

@register.inclusion_tag('cpm2013/tags/mainmenu.html')
def mainmenu(path):
    cur_lang = translation.get_language().split('-')[0]
    languages = sorted(
        settings.LANGUAGES,
        key=lambda lang: lang[0] == cur_lang
    )

    mainmenu_items = [
        (title, url, url == path) for title, url in MAINMENU_ITEMS
    ]
    
    return {
        'mainmenu_items': mainmenu_items,
        'languages': languages,
    }