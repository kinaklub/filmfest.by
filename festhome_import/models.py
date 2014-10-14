from collections import namedtuple

from datetime import datetime
from django.db import models

from submissions.constants import COUNTRIES
from submissions.models import Submission


FesthomeData = namedtuple(
    'FesthomeSubmission',
    ' '.join([
        'no',
        'festhome_id',
        'title',
        'title_en',
        'f_E',
        'length',
        'f_G',
        'f_H',
        'section',
        'status',
        'applicant_name',
        'applicant_lastname',
        'applicant_date_of_birth',
        'applicant_code',
        'applicant_phone',
        'applicant_email',
        'applicant_street',
        'applicant_city',
        'applicant_postal_code',
        'applicant_state',
        'applicant_country',
        'org_name',
        'org_email',
        'org_street',
        'org_city',
        'org_postal_code',
        'org_state',
        'org_country',
        'f_AC',
        'f_AD',
        'f_AE',
        'country',
        'date',
        'f_AH',
        'categories',
        'genre',
        'theme',
        'orig_lang',
        'f_AM',
        'f_AN',
        'f_AO',
        'f_AP',
        'f_AQ',
        'f_AR',
        'synopsis',
        'f_AT',
        'f_AU',
        'f_AV',
    ])
)


COUNTRIES_DICT = dict((unicode(v), k) for k, v in COUNTRIES)
COUNTRIES_DICT['Russia'] = 'RU'
COUNTRIES_DICT['United Kingdom'] = 'GB'
COUNTRIES_DICT['Macedonia'] = 'MK'
COUNTRIES_DICT['United States'] = 'US'
COUNTRIES_DICT['Iran'] = 'IR'
COUNTRIES_DICT['Montegro'] = 'ME'
COUNTRIES_DICT['Serbia'] = 'RS'
COUNTRIES_DICT['Kosovo'] = 'RS'
COUNTRIES_DICT[u'\u0411\u0435\u043b\u043e\u0440\u0443\u0441\u0441\u0438\u044f'] = 'BY'
COUNTRIES_DICT[u'\u0420\u043e\u0441\u0441\u0438\u044f'] = 'RU'
COUNTRIES_DICT[u'\u0423\u043a\u0440\u0430\u0438\u043d\u0430'] = 'UA'

COUNTRIES_DICT['SpainUnited Kingdom'] = 'ES'
COUNTRIES_DICT['ArgentinaSpain'] = 'AR'
COUNTRIES_DICT['SpainUnited States'] = 'ES'
COUNTRIES_DICT['CanadaCroatia'] = 'CA'
COUNTRIES_DICT['PeruSpain'] = 'PE'
COUNTRIES_DICT['GermanyIsrael'] = 'DE'
COUNTRIES_DICT['BelgiumFrance'] = 'BE'
COUNTRIES_DICT['BrazilPortugal'] = 'BR'
COUNTRIES_DICT['Spain (Canary, Ceuta & Melilla)'] = 'ES'
COUNTRIES_DICT['BahrainUnited Arab Emirates'] = 'BH'
COUNTRIES_DICT['SwitzerlandUnited StatesZambia'] = 'CH'
COUNTRIES_DICT['QatarSpain'] = 'QA'
COUNTRIES_DICT['Korea, South'] = 'KR'


SECTION_DICT = {
    'Documentary Films': 3,
}


class FesthomeSubmission(models.Model):
    submission = models.ForeignKey(Submission)
    festhome_id = models.IntegerField(db_index=True)

    @classmethod
    def from_data(cls, festhome_data):
        submission = Submission(
            title=festhome_data.title,
            title_en=festhome_data.title_en,
            country=COUNTRIES_DICT.get(festhome_data.country, 'ZZ'),
            section=SECTION_DICT.get(festhome_data.section, 1),
            synopsis=festhome_data.synopsis,
            length=festhome_data.length,
            aspect_ratio=' ',
            year=datetime.strptime(festhome_data.date, '%Y-%m-%d').year,
            premiere=2,  # no
            budget=' ',
            attend=0,
            allow_tv=2,
            allow_noncommercial=2,
            allow_network=2,
            backlink=12,  # other
            applicant='%s %s' % (
                festhome_data.applicant_name,
                festhome_data.applicant_lastname
            ),
            applicant_email=festhome_data.applicant_email,
            applicant_phone='(%s) %s' % (
                festhome_data.applicant_code,
                festhome_data.applicant_phone
            ),
            applicant_address='%s, %s, %s, %s' % (
                festhome_data.applicant_street,
                festhome_data.applicant_city,
                festhome_data.applicant_state,
                festhome_data.applicant_country
            ),
            director='%s %s' % (
                festhome_data.applicant_name,
                festhome_data.applicant_lastname
            ),
            director_email=festhome_data.applicant_email,
            director_address='%s, %s, %s, %s' % (
                festhome_data.applicant_street,
                festhome_data.applicant_city,
                festhome_data.applicant_state,
                festhome_data.applicant_country
            ),
            comment='Import from Festhome',
        )
        submission.save()
        return cls(
            submission=submission,
            festhome_id=festhome_data.festhome_id
        )

