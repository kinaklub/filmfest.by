# -*- coding: utf-8 -*-
from django import template

from apps.cpm2014.models import NewsEntry


register = template.Library()


@register.inclusion_tag('cpm2014/tags/news.html')
def cpm2014_news():
    news = NewsEntry.objects.language().order_by('-added_at')[:10]
    return {'news': news}
