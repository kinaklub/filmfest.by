from django.db import models
from django.utils.translation import ugettext_lazy as _

from cpm.constants import CAPACITY, COUNTRIES, KIND


class ScreeningPlaceProposal(models.Model):
    name_or_title = models.CharField(verbose_name=_(u'Your name or title'),
                                     max_length=1000)
    email = models.CharField(verbose_name=_(u'Email'), max_length=1000)
    phone = models.CharField(verbose_name=_(u'Tel.'),
                             max_length=1000, blank=True)
    url = models.CharField(verbose_name=_(u'URL'),
                           max_length=1000, blank=True)

    country = models.CharField(verbose_name=_(u'Country'),
                               max_length=2, choices=COUNTRIES)
    city = models.CharField(verbose_name=_(u'City / Town / Village'),
                            max_length=1000)
    kind = models.CharField(verbose_name=_(u'Who you are'),
                            choices=KIND.CHOICES, max_length=110)

    venue = models.TextField(verbose_name=_(u'Probable venue description'))
    capacity = models.CharField(verbose_name=_(u'Venue capacity'),
                                choices=CAPACITY.CHOICES,
                                max_length=2,
                                blank=True)
    ticket_price = models.CharField(
        verbose_name=_(u'Ticket price (estimated)'),
        max_length=110
    )
    screenings_amount = models.CharField(
        verbose_name=_(u'Amount of screenings (estimated)'),
        max_length=110,
        blank=True
    )
    proposals = models.TextField(verbose_name=_(u'Your proposals'), blank=True)
