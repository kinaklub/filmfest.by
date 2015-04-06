# -*- coding: utf-8 -*-
from collections import defaultdict

from django import template

from apps.cpm2014.models import NewsEntry
from events.models import Event


register = template.Library()


@register.inclusion_tag('cpm2014/tags/news.html')
def cpm2014_news():
    news = NewsEntry.objects.language().order_by('-added_at')[:10]
    return {'news': news}


@register.inclusion_tag('cpm2014/tags/timetable.html')
def cpm2014_timetable():
    # this query requires a lot of subqueries later...
    # but I have no time to find a workaround for hvad
    future_events = Event.objects.language().all()
    future_events = future_events.order_by('starts_at')

    cities = defaultdict(lambda: defaultdict(list))
    for event in future_events:
        cities[event.place.city][event.starts_at.date()].append(event)

    timetable = sorted(
        (
            (
                city,
                sorted(days.iteritems(), key=lambda x: x[0])
            ) for city, days in cities.iteritems()
        ),
        key=lambda x: -x[0].priority
    )

    return {'timetable': timetable}
