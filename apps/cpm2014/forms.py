from django.utils.translation import ugettext_lazy as _
from django import forms
from django.forms.util import ErrorList

from form_utils.forms import BetterModelForm

from apps.cpm2014.models import Submission, SubmissionTranslation
from validators import validate_checked


class InlineErrorList(ErrorList):
    def as_inline(self):
        if not self:
            return u''
        return ' '.join(unicode(e) for e in self)


class SubmissionForm(BetterModelForm):
    director_email = forms.EmailField(label="Email")
    applicant_email = forms.EmailField(label="Email")
    producer_email = forms.EmailField(label="Email")
    
    i_read_rules = forms.BooleanField(
        label=_('I have read the rules of the festival and '\
                'agree to its terms'),
        required=False, validators=[validate_checked])
    i_have_rights = forms.BooleanField(
        label=_('I declare that I am the legal owner of '\
                'all rights relating to the submitted movie'),
        required=False, validators=[validate_checked])

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('error_class', InlineErrorList)
        super(SubmissionForm, self).__init__(*args, **kwargs)

        for field_name in [
            'synopsis', 'film_awards', 'director_awards', 'director_address',
            'producer_address', 'other_credits', 'other_credits',
            'applicant_address'
        ]:
            self.fields[field_name].widget.attrs['rows'] = 4

    class Meta:
        model = Submission
        fieldsets = [
            ('film', {
                'fields': ['title', 'title_en', 'country', 'language', 'genre',
                           'section', 'synopsis', 'length', 'aspect_ratio',
                           'year', 'premiere', 'film_awards',
                           'budget', 'film_link', 'backlink'],
                'legend': _('Film'),
            }),
            ('director', {
                'fields': ['director', 'director_address', 'director_email',
                           'director_site', 'director_phone',
                           'director_awards'],
                'legend': _('Director'),
            }),
            ('producer', {
                'fields': ['producer', 'producer_address', 'producer_email',
                           'producer_site', 'producer_phone'],
                'legend': _('Producer'),
            }),
            ('credits', {
                'fields': ['screenwriter', 'editor', 'music',
                           'director_photography', 'other_credits'],
                'legend': _('Credits'),
            }),
            ('applicant', {
                'fields': ['applicant', 'applicant_address', 'applicant_email',
                           'applicant_site', 'applicant_phone', 'attend'],
                'legend': _('Applicant'),
            }),
            ('permissions', {
                'fields': ['allow_tv', 'allow_noncommercial', 'allow_network',
                           'i_read_rules', 'i_have_rights'],
                'legend': _('Permissions'),
            }),
        ]


class FieldsForm(forms.Form):
    fields = forms.MultipleChoiceField(
        choices=[(f.name, f.name) for f in Submission._meta.fields],
        widget=forms.CheckboxSelectMultiple
    )

    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None,
                 initial=None, error_class=ErrorList, label_suffix=':',
                 empty_permitted=False):
        if initial is None:
            initial = {
                'fields': [f.name for f in Submission._meta.fields]
            }
        super(FieldsForm, self).__init__(
            data, files, auto_id, prefix, initial, error_class,
            label_suffix, empty_permitted
        )


class SubmissionTranslationForm(forms.ModelForm):
    class Meta:
        model = SubmissionTranslation
        fields = ['title', 'genre', 'synopsis', 'synopsis_short', 'director']

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('error_class', InlineErrorList)
        super(SubmissionTranslationForm, self).__init__(*args, **kwargs)
