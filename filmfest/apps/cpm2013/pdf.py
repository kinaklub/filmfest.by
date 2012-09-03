import re
import os.path

from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from tex import latex2pdf

from apps.cpm2013.models import Submission

_REPLACE_RULES = {
    '#': '\\#',
    '$': '\\$',
    '%': '\\%',
    '&': '\\&',
    '~': '\\~{}',
    '_': '\\_',
    '^': '\\^{}',
    '\\': '\\textbackslash{}',
    '{': '\\{',
    '}': '\\}',
    '\r': '',
    '\n': ' ',
}
_RE = re.compile(
    '[%s]' % ''.join(
        re.escape(key) for key in _REPLACE_RULES.iterkeys()
    )
)
def _escape_latex_symbol(matchobj):
    return _REPLACE_RULES[matchobj.group(0)]
def latex_escape(value):
    return _RE.sub(_escape_latex_symbol, unicode(value))

SUBMIT_CONFIRMATION = [
    (_('Film'), [
        'title', 'title_en', 'country', 'language', 'genre',
        'section', 'synopsis', 'length', 'aspect_ratio',
        'year', 'premiere', 'film_awards', 'budget']),
    (_('Director'), [
        'director', 'director_address', 'director_email',
        'director_site', 'director_phone', 'director_awards']),
    (_('Producer'), [
        'producer', 'producer_address', 'producer_email',
        'producer_site', 'producer_phone']),
    (_('Applicant'), [
        'applicant', 'applicant_address', 'applicant_email',
        'applicant_site', 'applicant_phone', 'attend']),
    (_('Permissions'), [
        'allow_tv', 'allow_noncommercial', 'allow_network']),
]
def _get_confirmation_fields_latex(sections):
    sections_tex = []
    for section, cv_items in sections:
        if not any(value for name, value in cv_items):
            continue

        cv_items_latex = '\n'.join(
            '\cvitem{%s}{%s}' % (latex_escape(n), latex_escape(v)) \
            for n,v in cv_items if not (v is None or v == '')
        )

        sections_tex.append('\section{%s}\n%s' % (
            latex_escape(section), cv_items_latex
        ))

    return '\n'.join(sections_tex)


def get_submission_confirmation_report(submission):
    sections = []
    for section, fields in SUBMIT_CONFIRMATION:
        cv_items = []
        for field in fields:
            model_field = Submission._meta.get_field_by_name(field)[0]
            name = model_field.verbose_name
            if getattr(model_field, 'choices', None):
                value = getattr(submission, 'get_%s_display' % field)()
            else:
                value = getattr(submission, field)
            cv_items.append((name, value))

        sections.append((section, cv_items))


    with open(os.path.join(settings.PROJECT_ROOT, 'apps', 'cpm2013', 'docs',
                           'submission.tex')) as submission_head:
        latex_data = submission_head.read() % (
            _get_confirmation_fields_latex(sections),
        )

    return latex2pdf(latex_data)
