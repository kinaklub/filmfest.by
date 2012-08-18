from django.contrib import admin

from hvad.admin import TranslatableAdmin

from apps.cpm2013.models import NewsEntry

class NewsAdmin(TranslatableAdmin):
    pass
admin.site.register(NewsEntry, NewsAdmin)