from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static

from apps.cpm2012 import urls as cpm2012_urls
from apps.cpm2013 import urls as cpm2013_urls
from apps.cpm2014 import urls as cpm2014_urls

from django.contrib import admin
admin.autodiscover()

import djcelery
djcelery.setup_loader()

urlpatterns = i18n_patterns('',
    # Examples:
    # url(r'^$', 'filmfest.views.home', name='home'),
    # url(r'^filmfest/', include('filmfest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^2012/', include(cpm2012_urls)),
    url(r'^2013/', include(cpm2013_urls)),
    url(r'^2014/', include(cpm2014_urls)),

    url(r'^', include('cms.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
