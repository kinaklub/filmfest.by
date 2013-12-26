from django.contrib import admin

from cpm.models import ScreeningPlaceProposal


class ScreeningPlaceProposalAdmin(admin.ModelAdmin):
    list_display = [
        'name_or_title', 'email', 'url', 'country', 'city',
        'capacity', 'ticket_price', 'screenings_amount',
        'proposals', 'comment'
    ]
    readonly_fields = [
        'name_or_title', 'email', 'phone', 'url', 'country', 'city',
        'kind', 'venue', 'capacity', 'ticket_price', 'screenings_amount',
        'proposals',
    ]
    fields = readonly_fields + ['comment']

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(ScreeningPlaceProposal,
                    ScreeningPlaceProposalAdmin)
