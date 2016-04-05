from django.conf.urls import url, patterns

from cpm import views


urlpatterns = patterns('',
#    url(r'^venue/new/$', views.new_screening_place, name='new_screening_place'),  # noqa
    url(r'^partners/$', views.partners, name='partners'),
)
