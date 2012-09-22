from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_for_escaping

from hvad.admin import TranslatableAdmin

from apps.cpm2013.models import Submission, NewsEntry, Page

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['title', 'applicant_email', 'display_film_link']

    fieldsets = [
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
    
    def display_film_link(self, obj):
        if not obj.film_link:
            return '---'
        return '<a href="%(link)s">%(link)s</a>' % {
            'link': mark_for_escaping(obj.film_link)
        }
    display_film_link.short_description = _('Download link')
    display_film_link.allow_tags = True

class NewsAdmin(TranslatableAdmin):
    pass
class PageAdmin(TranslatableAdmin):
    pass

admin.site.register(Submission, SubmissionAdmin)
admin.site.register(NewsEntry, NewsAdmin)
admin.site.register(Page, PageAdmin)