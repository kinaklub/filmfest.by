import io
import re
import os.path
from cStringIO import StringIO

from django.utils.translation import ugettext_lazy as _
from django.utils import translation
from django.conf import settings

from apps.cpm2013.constants import APP_ROOT
from apps.cpm2013.models import Submission


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
]
SUBMIT_CONFIRMATION_PERMISSIONS = [
    'allow_tv', 'allow_noncommercial', 'allow_network'
]

SUBMISSION_RST = {
    'en': 'submission_en.rst',
    'be': 'submission_be.rst',
    'ru': 'submission_ru.rst',
}
DEFAULT_SUBMISSION_RST = SUBMISSION_RST['en']

def _escape_rst(value):
    lines = []
    for line in unicode(value).split('\n'):
        lines.append(
            ''.join(
                '\%s' % c if c != ' ' else c for\
                c in line.strip()
            )
        )
    return '\n\n'.join(lines)

def _get_rst_fields(sections, permissions):
    sections_rst = []
    for section, cv_items in sections:
        if not any(value for name, value in cv_items):
            continue

        section_rst = '\n'.join(
            u'* %s\n    %s' % (
                n,
                '\n    '.join(_escape_rst(v).split('\n'))
            ) \
            for n,v in cv_items if not (v is None or v == '')
        )

        sections_rst.append(u'\n%s\n%s\n\n%s' % (
            section, '-' * len(section), section_rst
        ))

    for section, cv_items in permissions:
        section_rst = '\n\n'.join(
            '* ' + _escape_rst(name) for name in cv_items
        )
        sections_rst.append(u'\n%s\n%s\n\n%s' % (
            section, '-' * len(section), section_rst
        ))
        
    return {
        'sections': '\n'.join(sections_rst),
    }


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

    permissions = []
    for field in SUBMIT_CONFIRMATION_PERMISSIONS:
        value = getattr(submission, field)
        if value != 1:
            continue

        model_field = Submission._meta.get_field_by_name(field)[0]
        name = model_field.verbose_name
        permissions.append(name)
    if permissions:
        permissions = [(_('Permissions'), permissions)]


    docs = os.path.join(APP_ROOT, 'docs')
    lang = translation.get_language().lower()
    submission_rst = os.path.join(
        docs, SUBMISSION_RST.get(lang, DEFAULT_SUBMISSION_RST))
    with io.open(submission_rst, encoding='utf-8') as submission_head:
        rst_data = submission_head.read() % _get_rst_fields(
            sections, permissions)

    from rst2pdf.createpdf import RstToPdf
    pdf_creator = RstToPdf(
        stylesheets=[os.path.join(docs, 'submission2.stylesheet')],
        font_path=['/usr/share/fonts/TTF/'],
        breaklevel=0,
    )

    with io.open('/tmp/cpm.rst', 'w', encoding='utf-8') as w:
        w.write(rst_data)
    pdf_content = StringIO()
    pdf_creator.createPdf(text=rst_data, output=pdf_content)
    return pdf_content.getvalue()
