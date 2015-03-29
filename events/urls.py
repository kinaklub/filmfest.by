from django.conf.urls import url, patterns

from events import views


urlpatterns = patterns('',
    url(r'^program/list/$',
        views.program_list,
        name='events_program_list'),
    url(r'^program/add/$',
        views.program_edit,
        name='events_program_add'),
    url(r'^program/(?P<program_id>\d+)/$',
        views.program_details,
        name='events_program_details'),
    url(r'^program/(?P<program_id>\d+)/edit/$',
        views.program_edit,
        name='events_program_edit'),
    url(r'^event/(?P<event_id>\d+)/$',
        views.event_details,
        name='events_event_details'),
)
