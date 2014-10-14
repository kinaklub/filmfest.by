from django.conf.urls import url, patterns

from festhome_import import views


urlpatterns = patterns('',
    url(r'^import/$', views.import_festhome, name='festhome_import'),
)
