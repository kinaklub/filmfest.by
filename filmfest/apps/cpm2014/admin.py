from functools import update_wrapper
from itertools import chain, islice
import os
import os.path
import tempfile

from django.conf import settings
from django.contrib import admin
from django.db.models import Count
from django.utils.translation import ugettext_lazy as _
from django.utils import translation
from django.utils.html import escape
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template.defaultfilters import linebreaksbr
from django.template.defaultfilters import urlizetrunc
from django.template import RequestContext
from django.core.exceptions import PermissionDenied
from django.contrib.admin.util import unquote
from django.db import transaction
from django.core.urlresolvers import reverse

from hvad.admin import TranslatableAdmin
from hvad.utils import get_translation_aware_manager

import openpyxl

from apps.cpm2014.models import Submission, Prescreening, NewsEntry
from apps.cpm2014.forms import FieldsForm


class PreviewFilter(admin.SimpleListFilter):
    title = _('Previewed')

    parameter_name = 'prv'

    def lookups(self, request, model_admin):
        return (
            ('1', _('Yes')),
            ('0', _('No')),
        )

    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.filter(preview=None)
        if self.value() == '1':
            return queryset.exclude(preview=None)


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['title', 'applicant_email', 'display_film_link',
                    'submitted_at', 'display_country',
                    'display_facts', 'display_comment']
    save_on_top = True

    fieldsets = [
            (_('Comments'), {
                'fields': ['comment', 'comment_email_sent',
                           'comment_film_received', 'comment_papers_received',
                           'comment_vob_received',]
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

    def queryset(self, request):
        qs = Submission.objects.all().order_by('-id')
        qs = qs.annotate(num_prescreenings=Count('prescreening'))
        return qs

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
            url(r'^xlsx/$',
                wrap(self.xlsx_view),
                name='%s_%s_xlsx' % info),
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
        result.append(u'%s: %s' % (
            _('Prescreenings'),
            obj.num_prescreenings and true_html or false_html
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

    def xlsx_view(self, request):
        if not self.has_change_permission(request):
            raise PermissionDenied

        form = FieldsForm(request.POST or None)
        if request.method == 'POST' and form.is_valid():
            xlsx_file = tempfile.mktemp()
            current_lang = translation.get_language()

            try:
                submissions = Submission.objects.all().order_by('id')

                translation.activate('en')

                from openpyxl import Workbook
                wb = Workbook(optimized_write = True)
                ws = wb.create_sheet()

                ws.append(form.cleaned_data['fields'])
                for s in submissions:
                    row = []
                    for field in form.cleaned_data['fields']:
                        try:
                            row.append(getattr(s, 'get_%s_display' % field)())
                        except AttributeError:
                            row.append(getattr(s, field))
                    ws.append(row)
                wb.save(xlsx_file)
                with open(xlsx_file, 'r') as f:
                    xlsx = f.read()
            finally:
                translation.activate(current_lang)
                if os.path.exists(xlsx_file):
                    os.unlink(xlsx_file)
            response = HttpResponse(
                xlsx,
                content_type='application/vnd.openxmlformats-officedocument.'\
                'spreadsheetml.sheet'
            )
            response['Content-Disposition'] = 'attachment; '\
                               'filename="submissions.xlsx"'
            return response

        return render_to_response(
            'admin/cpm2013/submission/xlsx.html',
            {'form': form},
            context_instance=RequestContext(request),
        )


class PrescreeningAdmin(admin.ModelAdmin):
    list_display = ['id', 'datetime']
    filter_horizontal = ['submissions']

class NewsAdmin(TranslatableAdmin):
    list_display = ['display_title', 'added_at']

    def queryset(self, request):
        return get_translation_aware_manager(NewsEntry)

    def display_title(self, obj):
        return obj.title
    display_title.short_description = _('Title')


admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Prescreening, PrescreeningAdmin)
admin.site.register(NewsEntry, NewsAdmin)
