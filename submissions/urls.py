from django.conf.urls import url, patterns

from submissions import views


urlpatterns = patterns('',
    url(r'^submit/$', views.submit, name='submissions_submit'),
)
