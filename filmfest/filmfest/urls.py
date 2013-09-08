from django.conf.urls import patterns, include, url

from apps.cpm2012 import urls as cpm2012_urls
from apps.cpm2013 import urls as cpm2013_urls
from apps.cpm2014 import urls as cpm2014_urls

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
    url(r'^cms/', include('cms.urls')),

    url(r'^2012/', include(cpm2012_urls)),
    url(r'^2013/', include(cpm2013_urls)),
    url(r'^2014/', include(cpm2014_urls)),
    url(r'^(?P<lang_code>[\-\w]+)/.*', 'apps.cpm_common.views.set_language', name='cpm_set_language'),

    url(r'^$', 'filmfest.views.index', name='index'),
)
