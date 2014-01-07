from django.utils.translation import ugettext_lazy as _

# TODO: import refactoring
from apps.cpm2014.constants import COUNTRIES


__all__ = ['CAPACITY', 'COUNTRIES', 'KIND', 'TICKET_PRICE']


class KIND:
    INDIVIDUAL = 'Individual'
    COMMUNITY = 'Community'
    FESTIVAL = 'Festival'
    FILM_CLUB = 'Film club'
    CINEMA_CAFE = 'Cinema caffe'
    EDUCATIONAL_INSTITUTION = 'Educational institution'
    DISTRIBUTION_COMPANY = 'Distribution company'
    ART_OBJECT = 'Art space / Gallery / Museum'
    CINEMA_THEATRE = 'Cinema theatre'
    OTHER = 'Other'

    MAX_LENGTH = 100

    CHOICES = (
        (INDIVIDUAL, _('Individual')),
        (COMMUNITY, _(u'Community')),
        (FESTIVAL, _(u'Festival')),
        (FILM_CLUB, _(u'Film club')),
        (CINEMA_CAFE, _(u'Cinema caffe')),
        (EDUCATIONAL_INSTITUTION, _(u'Educational institution')),
        (DISTRIBUTION_COMPANY, _(u'Distribution company')),
        (ART_OBJECT, _(u'Art space / Gallery / Museum')),
        (CINEMA_THEATRE, _(u'Cinema theatre')),
        (OTHER, _(u'Other')),
    )


class CAPACITY:
    SMALL = '<50'
    MEDIUM = '50-150'
    LARGE = '150-500'
    HUGE = '>500'

    CHOICES = (
        (SMALL, _(u'< 50 seats')),
        (MEDIUM, _(u'50 - 150 seats')),
        (LARGE, _(u'150 - 500 seats')),
        (HUGE, _(u'> 500 seats')),
    )


class TICKET_PRICE:
    FREE = 'Free'
    OTHER = 'Other'

    MAX_LENGTH = 100

    CHOICES = (
        (FREE, _(u'Free')),
        (OTHER, _(u'Other')),
    )
