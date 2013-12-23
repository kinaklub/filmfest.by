from django.contrib import admin

from cpm.models import ScreeningPlaceProposal


class ScreeningPlaceProposalAdmin(admin.ModelAdmin):
    list_display = [
        'name_or_title', 'email', 'url', 'country', 'city',
        'capacity', 'ticket_price', 'screenings_amount',
        'proposals',
    ]
    fields = [
        'name_or_title', 'email', 'phone', 'url', 'country', 'city',
        'kind', 'venue', 'capacity', 'ticket_price', 'screenings_amount',
        'proposals',
    ]
    readonly_fields = fields


admin.site.register(ScreeningPlaceProposal,
                    ScreeningPlaceProposalAdmin)
