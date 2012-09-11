from django.contrib import admin

from hvad.admin import TranslatableAdmin

from apps.cpm2013.models import Submission, NewsEntry, Page

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['title', 'applicant_email']
class NewsAdmin(TranslatableAdmin):
    pass
class PageAdmin(TranslatableAdmin):
    pass

admin.site.register(Submission, SubmissionAdmin)
admin.site.register(NewsEntry, NewsAdmin)
admin.site.register(Page, PageAdmin)