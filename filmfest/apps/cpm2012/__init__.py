def get_urls():
    from django.conf.urls import patterns, include, url
    from django.views.generic.simple import direct_to_template

    return patterns('',
        url(r'^$', direct_to_template, {'template': 'cpm2012/index.html'}, name='index'),
        url(r'^cast/$', direct_to_template, {'template': 'cpm2012/cast.html'}, name='casr'),
    )

urls = (get_urls(), 'cpm2012', 'cpm2012')