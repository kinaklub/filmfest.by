from django import forms
from django.forms.util import ErrorList
from django.utils.translation import ugettext_lazy as _

from submissions.models import Submission
from events.models import Program, ProgramTranslation


class InlineErrorList(ErrorList):
    def as_inline(self):
        if not self:
            return u''
        return ' '.join(unicode(e) for e in self)


class ProgramForm(forms.ModelForm):
    films = forms.CharField(
        label=_(u'Films'), help_text=_(u'Submission IDs, one per line'),
        widget=forms.Textarea
    )

    class Meta:
        model = Program
        fields = ['code', 'section']

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('error_class', InlineErrorList)
        super(ProgramForm, self).__init__(*args, **kwargs)

    def clean_films(self):
        value = self.cleaned_data['films']
        raw_films = [
            film.strip() for film in value.split('\n') if film.strip()
        ]
        for film in raw_films:
            if not film.isdigit():
                raise forms.ValidationError(
                    '"%s" is an invalid submission ID' % film
                )

        film_ids = [int(film) for film in raw_films]

        submissions = Submission.objects.in_bulk(film_ids)
        if len(film_ids) != len(submissions):
            not_found = ', '.join(
                str(f) for f in set(film_ids) - set(submissions)
            )
            raise forms.ValidationError(
                'Submissions not found: %s' % not_found
            )

        return [submissions[film_id] for film_id in film_ids]


class ProgramTranslationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProgramTranslationForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget = forms.Textarea()

    class Meta:
        model = ProgramTranslation
        fields = ['name', 'description']
