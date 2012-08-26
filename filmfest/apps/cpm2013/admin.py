from django.contrib import admin

from hvad.admin import TranslatableAdmin

from apps.cpm2013.models import NewsEntry, Page

class NewsAdmin(TranslatableAdmin):
    pass
class PageAdmin(TranslatableAdmin):
    pass

admin.site.register(NewsEntry, NewsAdmin)
admin.site.register(Page, PageAdmin)