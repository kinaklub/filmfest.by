from django.conf.urls import patterns, include, url

from apps.cpm2012 import urls as cpm2012_urls
from apps.cpm2013 import urls as cpm2013_urls

from django.contrib import admin
admin.autodiscover()

import djcelery
djcelery.setup_loader()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'filmfest.views.home', name='home'),
    # url(r'^filmfest/', include('filmfest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^2012/', include(cpm2012_urls)),
    url(r'^2013/', include(cpm2013_urls)),
    (r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^$', 'filmfest.views.index', name='index'),
)
