def get_urls():
    from django.conf.urls import patterns, include, url
    from django.views.generic.simple import direct_to_template

    from apps.cpm2013 import views

    return patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^page/(?P<slug>[\w\d_]+)', views.page, name='page'),
        url(r'^volunteers/questionnaire', direct_to_template,
            {'template': 'cpm2013/volunteers_questionnaire.html'},
            name='volunteers_questionnaire'),
        url(r'^rules/(?P<lang>\w{2})', views.rules, name='rules_lang'),
        url(r'^rules', views.rules, name='rules'),
        url(r'^submit', views.submit, name='submit'),
        url(r'^contacts', direct_to_template,
            {'template': 'cpm2013/contacts.html'},
            name='contacts'),
    )

urls = (get_urls(), 'cpm2013', 'cpm2013')
