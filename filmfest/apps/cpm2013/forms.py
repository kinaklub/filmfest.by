from django.utils.translation import ugettext as _
from django import forms
from django.forms.util import ErrorList

from form_utils.forms import BetterModelForm

from models import Submission
from validators import validate_checked


class InlineErrorList(ErrorList):
    def as_inline(self):
        if not self:
            return u''
        return ' '.join(unicode(e) for e in self)


class SubmissionForm(BetterModelForm):
    i_read_rules = forms.BooleanField(
        required=False, validators=[validate_checked])
    i_have_rights = forms.BooleanField(
        required=False, validators=[validate_checked])

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('error_class', InlineErrorList)
        super(SubmissionForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Submission
        fieldsets = [
            ('film', {
                'fields': ['title', 'title_en', 'country', 'language',
                           'section', 'synopsis', 'length', 'aspect_ratio',
                           'year', 'premiere', 'film_awards',
                           'budget'],
                'legend': _ ('Film'),
            }),
            ('director', {
                'fields': ['director', 'director_address', 'director_email',
                           'director_site', 'director_phone',
                           'director_awards'],
                'legend': _ ('Director'),
            }),
            ('producer', {
                'fields': ['producer', 'producer_address', 'producer_email',
                           'producer_site', 'producer_phone'],
                'legend': _ ('Producer'),
            }),
            ('owner', {
                'fields': ['owner', 'owner_address', 'owner_email',
                           'owner_site', 'owner_phone'],
                'legend': _ ('Rights holder'),
            }),
            ('distributor', {
                'fields': ['distributor', 'distributor_address',
                           'distributor_email', 'distributor_site',
                           'distributor_phone'],
                'legend': _ ('Distributor'),
            }),
            ('applicant', {
                'fields': ['applicant', 'applicant_address', 'applicant_email',
                           'applicant_site', 'applicant_phone', 'attend'],
                'legend': _ ('Applicant'),
            }),
            ('permissions', {
                'fields': ['allow_tv', 'allow_noncommercial', 'allow_network',
                           'i_read_rules', 'i_have_rights'],
                'legend': _ ('Permissions'),
            }),
        ]
