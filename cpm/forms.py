from django import forms
from django.forms.util import ErrorList

from cpm.constants import KIND
from cpm.models import ScreeningPlaceProposal


class InlineErrorList(ErrorList):
    def as_inline(self):
        if not self:
            return u''
        return ' '.join(unicode(e) for e in self)



class ScreeningPlaceProposalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('error_class', InlineErrorList)
        super(ScreeningPlaceProposalForm, self).__init__(*args, **kwargs)

        for field_name in ['venue', 'proposals']:
            self.fields[field_name].widget.attrs['rows'] = 4

    class Meta:
        model = ScreeningPlaceProposal
        fields = [
            'name_or_title', 'email', 'phone', 'url', 'country', 'city',
            'kind', 'venue', 'capacity', 'ticket_price', 'screenings_amount',
            'proposals',
        ]
