def get_urls():
    from django.conf.urls import patterns, include, url
    from django.views.generic.simple import direct_to_template

    from apps.cpm2013 import views

    return patterns('',
        url(r'^page/(?P<slug>[\w\d_]+)', views.page, name='page'),
        url(r'^', views.index, name='index'),
        # url(r'^volunteers/questionnaire', direct_to_template,
        #     {'template': 'cpm2013/volunteers_questionnaire.html'},
        #     name='volunteers_questionnaire'),
        # url(r'^rules/(?P<lang>\w{2})', views.rules, name='rules_lang'),
        # url(r'^rules', views.rules, name='rules'),
        # url(r'^submit', views.submit, name='submit'),
        # url(r'^partners', views.partners, name='partners'),
        # url(r'^contacts', direct_to_template,
        #     {'template': 'cpm2013/contacts.html'},
        #     name='contacts'),
        # url(r'^presskit', views.press_kit, name='press_kit'),
        # url(r'^submission/(?P<subm_id>[\d]+)/(?P<subm_hash>[\w\d]+)/$',
        #     views.submission_info, name='submission_info'),
        # url(r'^submission/(?P<subm_id>[\d]+)/(?P<subm_hash>[\w\d]+)/upload/',
        #     views.submission_info_upload, name='submission_info_upload'),
        # url(r'^programs/(?P<program_id>[\w\d_]+)',
        #     views.program, name='program'),
        # url(r'^programs',
        #     views.programs, name='programs'),
    )

urls = (get_urls(), 'cpm2013', 'cpm2013')
