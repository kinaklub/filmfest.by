# -*- coding: utf-8 -*-
from django import template
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils import translation
from django.conf import settings


register = template.Library()


def get_mainmenu_items():
    return [
        (_('Home'), reverse('pages-root',), ()),
        (
            _('Festival'),
            '',
            (
                (_('2012: good memories'), reverse('cpm2012:index')),
                (_('2013: good memories'), reverse('cpm2013:index')),
                (
                    _('Regulations'),
                    reverse('pages-details-by-slug', kwargs={'slug': 'rules'})
                ),
                (
                    _('Submit your film!'),
                    reverse('cpm2014:submit')
                ),
            )
        ),
        (
            _('Volunteers'),
            '',
            (
                (
                    _('Join in'),
                    reverse('pages-details-by-slug', kwargs={'slug': 'vklyuchajsya'})
                ),
                (
                    _('Discussion group'),
                    'http://groups.google.com/group/cpm2015'
                ),
                (
                    _('Volunteer form'),
                    'http://filmfest.by/ru/2013/page/volunteer_form'
                )
            )
        ),
        (
            _('Partners'),
            reverse('cpm2014:partners'),
            ()
        ),
        (
            _('Press-center'),
            '',
            (
                (
                    _('Press-kit'),
                    reverse('pages-details-by-slug', kwargs={'slug': 'press-kit'}),
                ),
                (
                    _('Festival in media'),
                    reverse('pages-details-by-slug', kwargs={'slug': 'media'})
                ),

            )
        ),
        (
            _('Contacts'),
            reverse('cpm2014:contacts'),
            ()
        ),
    ]


@register.inclusion_tag('cpm_common/tags/mainmenu.html')
def mainmenu(request):
    cur_lang = translation.get_language().split('-')[0]

    parts = request.get_full_path().split('/', 2)
    path = parts[2] if len(parts) > 2 else ''

    lang_url = lambda code: '/%s/%s' % (code, path)
    languages = [
        (
            code,
            name,
            lang_url(code),
            code == cur_lang
        ) for code, name in [
            ('en', u'English'),
            ('ru', u'Русский'),
            ('be', u'Беларуская'),
        ]
    ]

    mainmenu_items = []
    for title, url, children in get_mainmenu_items():
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
        'mainmenu_items': get_mainmenu_items(),
    }
