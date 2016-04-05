from collections import defaultdict

from django import template
from django.conf import settings

from events.models import Event


register = template.Library()


@register.inclusion_tag('cpm/tags/timetable.html')
def cpm_timetable():
    # this query requires a lot of subqueries later...
    # but I have no time to find a workaround for hvad
    future_events = Event.objects.language().all()
    future_events = future_events.order_by('starts_at')

    future_starts_at = getattr(settings, 'CPM_TIMETABLE_STARTS_DT', None)
    if future_starts_at:
        future_events = future_events.filter(starts_at__gte=future_starts_at)

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


@register.inclusion_tag('cpm/tags/banners_list.html')
def banners_list(banners):
    return {'banners': banners}
