def get_urls():
    from django.conf.urls import patterns, include, url

    import views

    return patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^rules/$', views.index, name='rules'),
        url(r'^submit/$', views.submit, name='submit'),
    )

urls = (get_urls(), 'cpm2013', 'cpm2013')
