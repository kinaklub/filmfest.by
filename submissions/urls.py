from django.conf.urls import url, patterns

from submissions import views
from submissions.constants import TRANSLATION_LANGUAGES


LANGS = '|'.join(code for code, name in TRANSLATION_LANGUAGES)


urlpatterns = patterns('',
    url(r'^submit/$',
        views.submit,
        name='submissions_submit'),
    url((
            r'^submission/(?P<submission_id>\d+)/'
            r'translation/(?P<lang>%s)$' % LANGS
        ),
        views.translation_details,
        name='submissions_translation_details'),
    url((
            r'^submission/(?P<submission_id>\d+)/'
            r'translation/(?P<lang>%s)/edit$' % LANGS
        ),
        views.translation_edit,
        name='submissions_translation_edit'),
    url(r'^translations/$',
        views.translations_all_json,
        name='submissions_translations_all_json'),
)
