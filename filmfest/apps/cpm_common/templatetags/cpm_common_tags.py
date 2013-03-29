# -*- coding: utf-8 -*-
from django import template
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils import translation
from django.conf import settings


register = template.Library()


MAINMENU_ITEMS = [
    (_('Home'), reverse('cpm2014:index'), ()),
    (_('Festival'), '', (
        (_('2012: good memories'), reverse('cpm2012:index')),
        (_('Festival in media'), reverse('cpm2013:page', args=['media'])),
    )),
    (_('Participants'), '', (
        (_('Regulations'), reverse('cpm2014:rules')),
        (_('Submit your film!'), reverse('cpm2014:submit')),
    )),
    (_('Volunteers'), '', (
        (_('Discussion group'), 'http://groups.google.com/group/cpm2014'),
    )),
    (_('Partners'), reverse('cpm2014:partners'), ()),
    (_('Press kit'), reverse('cpm2014:press_kit'), ()),
    (_('Contacts'), reverse('cpm2014:contacts'), ()),
]

@register.inclusion_tag('cpm_common/tags/mainmenu.html')
def mainmenu(request):
    cur_lang = translation.get_language().split('-')[0]
    lang_url = '/%%s%s' % request.get_full_path()
    languages = [(code, name, lang_url % code, code == cur_lang) for code, name in [
        ('en', 'English'),
        ('ru', 'Русский'),
        ('be', 'Беларуская'),
    ]]

    mainmenu_items = []
    for title, url, children in MAINMENU_ITEMS:
        active = False
        new_children = []
        for sub_title, sub_url in children:
            sub_active = (sub_url == request.path)
            active = active or sub_active
            new_children.append((sub_title, sub_url, sub_active))

        active = active or (url == request.path)
        mainmenu_items.append((title, url, new_children, active))
    
    return {
        'mainmenu_items': mainmenu_items,
        'languages': languages,
    }

@register.inclusion_tag('cpm_common/tags/bottommenu.html')
def bottommenu():
    return {
        'mainmenu_items': MAINMENU_ITEMS,
    }