from django.contrib import admin

from hvad.admin import TranslatableAdmin
from hvad.utils import get_translation_aware_manager

from events.models import City, Event, Place


class CityAdmin(TranslatableAdmin):
    list_display = ['code', 'priority']
    order_by = ('-priority',)

    queryset = lambda self, request: get_translation_aware_manager(City)


class PlaceAdmin(TranslatableAdmin):
    list_display = ['code', 'city']

    queryset = lambda self, request: get_translation_aware_manager(Place)


class EventAdmin(TranslatableAdmin):
    list_display = ['code', 'place', 'starts_at']

    queryset = lambda self, request: get_translation_aware_manager(Event)


admin.site.register(City, CityAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Event, EventAdmin)
