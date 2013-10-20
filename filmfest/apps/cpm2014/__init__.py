def get_urls():
    from django.conf.urls import patterns, include, url
    from django.views.generic.simple import direct_to_template

    from rest_framework import routers

    from apps.cpm2014 import views

    router = routers.DefaultRouter()
    router.register(r'submissions', views.SubmissionViewSet)

    return patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^rules/(?P<lang>\w{2})', views.rules, name='rules_lang'),
        url(r'^rules', views.rules, name='rules'),
        url(r'^submit', views.submit, name='submit'),
        url(r'^partners', views.partners, name='partners'),
        url(r'^contacts', direct_to_template,
            {'template': 'cpm2014/contacts.html'},
            name='contacts'),
        url(r'^presskit', views.press_kit, name='press_kit'),
        url(r'^api/', include(router.urls)),

        url(r'^angular/', 'cpm.views.angular'),
    )

urls = (get_urls(), 'cpm2014', 'cpm2014')
