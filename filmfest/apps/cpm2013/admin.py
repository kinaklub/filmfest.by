from functools import update_wrapper
from itertools import chain, islice

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils import translation
from django.utils.html import escape
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import linebreaksbr
from django.template.defaultfilters import urlizetrunc
from django.core.exceptions import PermissionDenied
from django.contrib.admin.util import unquote

from hvad.admin import TranslatableAdmin

from apps.cpm2013.models import Submission, NewsEntry, Page

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['title', 'applicant_email', 'display_film_link',
                    'submitted_at', 'display_country',
                    'display_facts', 'display_comment']
    list_filter = ['comment_email_sent', 'comment_film_received',
                   'comment_papers_received', 'comment_vob_received']
    ordering = ('-id',)

    fieldsets = [
            (_('Comments'), {
                'fields': ['comment', 'comment_email_sent',
                           'comment_film_received', 'comment_papers_received',
                           'comment_vob_received'],
            }),
            (_('Dates'), {
                'fields': ['submitted_at', 'email_sent_at',
                           'film_received_at', 'papers_received_at'],
            }),
            (_('Film'), {
                'fields': ['title', 'title_en', 'country', 'language', 'genre',
                           'section', 'synopsis', 'length', 'aspect_ratio',
                           'year', 'premiere', 'film_awards',
                           'budget', 'film_link', 'backlink'],
            }),
            (_('Director'), {
                'fields': ['director', 'director_address', 'director_email',
                           'director_site', 'director_phone',
                           'director_awards'],
            }),
            (_('Producer'), {
                'fields': ['producer', 'producer_address', 'producer_email',
                           'producer_site', 'producer_phone'],
            }),
            (_('Credits'), {
                'fields': ['screenwriter', 'editor', 'music',
                           'director_photography', 'other_credits'],
            }),
            (_('Applicant'), {
                'fields': ['applicant', 'applicant_address', 'applicant_email',
                           'applicant_site', 'applicant_phone', 'attend'],
            }),
            (_('Permissions'), {
                'fields': ['allow_tv', 'allow_noncommercial', 'allow_network'],
            }),
        ]

    readonly_fields = ['submitted_at']
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return self.readonly_fields

        return list(chain(*(
            fldst[1]['fields'] for fldst in islice(self.fieldsets, 1, None)
        )))

    def get_urls(self):
        from django.conf.urls import patterns, url

        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)
            return update_wrapper(wrapper, view)

        info = self.model._meta.app_label, self.model._meta.module_name

        return  patterns('',
            url(r'^(\d+)/pdf/$',
                wrap(self.pdf_view),
                name='%s_%s_pdf' % info),
        ) + super(SubmissionAdmin, self).get_urls()

    def display_film_link(self, obj):
        if not obj.film_link:
            return '---'
        return urlizetrunc(obj.film_link, 20)
    display_film_link.short_description = _('Download link')
    display_film_link.allow_tags = True

    def display_comment(self, obj):
        return linebreaksbr(obj.comment or '')
    display_comment.short_description = _('Comment')
    display_comment.allow_tags = True

    def display_country(self, obj):
        return obj.get_country_display()
    display_country.short_description = _('Country')

    def display_facts(self, obj):
        fields = ['comment_email_sent', 'comment_film_received',
                  'comment_papers_received', 'comment_vob_received']

        true_html = '<img alt="True" src="/static/admin/img/icon-yes.gif">'
        false_html = '<img alt="False" src="/static/admin/img/icon-no.gif">'
        result = []
        for field_name in fields:
            result.append(u'%s: %s' % (
                obj._meta.get_field_by_name(field_name)[0].verbose_name,
                getattr(obj, field_name) and true_html or false_html
            ))
        return '<br />'.join(result)
    display_facts.short_description = _('Facts')
    display_facts.allow_tags = True

    def pdf_view(self, request, object_id):
        obj = get_object_or_404(Submission, pk=unquote(object_id))
        if not self.has_change_permission(request, obj):
            raise PermissionDenied

        from apps.cpm2013.pdf import get_submission_confirmation_report

        current_lang = translation.get_language()
        try:
            translation.activate(obj.submission_language)
            pdf = get_submission_confirmation_report(obj)
        finally:
            translation.activate(current_lang)

        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="cpm2013.pdf"'

        return response


    
class NewsAdmin(TranslatableAdmin):
    pass
class PageAdmin(TranslatableAdmin):
    pass

admin.site.register(Submission, SubmissionAdmin)
admin.site.register(NewsEntry, NewsAdmin)
admin.site.register(Page, PageAdmin)