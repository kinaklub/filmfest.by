from itertools import chain, islice

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils.html import escape
from django.template.defaultfilters import linebreaksbr

from hvad.admin import TranslatableAdmin

from apps.cpm2013.models import Submission, NewsEntry, Page

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['title', 'applicant_email', 'display_film_link',
                    'submitted_at', 'display_country',
                    'comment_email_sent', 'comment_film_received',
                    'comment_papers_received', 'display_comment']
    list_filter = ['comment_email_sent', 'comment_film_received',
                   'comment_papers_received']
    ordering = ('-id',)

    fieldsets = [
            (_('Comments'), {
                'fields': ['comment', 'comment_email_sent',
                           'comment_film_received', 'comment_papers_received'],
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
    
    def display_film_link(self, obj):
        if not obj.film_link:
            return '---'
        return '<a href="%(link)s">%(link)s</a>' % {
            'link': escape(obj.film_link)
        }
    display_film_link.short_description = _('Download link')
    display_film_link.allow_tags = True

    def display_comment(self, obj):
        return linebreaksbr(obj.comment or '')
    display_comment.short_description = _('Comment')
    display_comment.allow_tags = True

    def display_country(self, obj):
        return obj.get_country_display()
    display_comment.short_description = _('Country')

    
class NewsAdmin(TranslatableAdmin):
    pass
class PageAdmin(TranslatableAdmin):
    pass

admin.site.register(Submission, SubmissionAdmin)
admin.site.register(NewsEntry, NewsAdmin)
admin.site.register(Page, PageAdmin)