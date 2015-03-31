from django.conf.urls import url, patterns, include
from rest_framework import routers

from submissions import views
from submissions.constants import TRANSLATION_LANGUAGES


LANGS = '|'.join(code for code, name in TRANSLATION_LANGUAGES)

router = routers.DefaultRouter()
router.register(r'submissions', views.SubmissionViewSet)

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
    url( r'^submission/api/', include(router.urls)),
)
