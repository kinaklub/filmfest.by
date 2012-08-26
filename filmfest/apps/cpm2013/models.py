from django.db import models
from django.utils.translation import ugettext as _

from hvad.models import TranslatableModel, TranslatedFields

from constants import YESNO, YESNOMAYBE, COUNTRIES, LANGUAGES,\
     SECTIONS, BACKLINKS


class Submission(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=1000)
    title_en = models.CharField(verbose_name=_('Title in English'),
                                max_length=1000)
    country = models.CharField(verbose_name=_('Country'),
                                max_length=2, choices=COUNTRIES)
    language = models.CharField(verbose_name=_('Language'),
                                max_length=10, choices=LANGUAGES)
    section = models.IntegerField(verbose_name=_('Section'),
                                  choices=SECTIONS)
    synopsis = models.TextField(verbose_name=_('Synopsis'))
    length = models.IntegerField(verbose_name=_('Length in minutes'))
    aspect_ratio = models.CharField(verbose_name=_('Aspect ratio'),
                                    max_length=1000)
    year = models.IntegerField(verbose_name=_('Year'))
    premiere = models.IntegerField(verbose_name=_('Premiere'), choices=YESNO)
    film_awards = models.TextField(
        verbose_name=_('Film awards'), blank=True)
    director_awards = models.TextField(
        verbose_name=_('Director awards'), blank=True)
    budget = models.CharField(verbose_name=_('Budget'), max_length=1000)
    attend = models.IntegerField(
        verbose_name=_('Are you going to attend the festival?'),
        choices=YESNOMAYBE, default=0)
    backlink = models.IntegerField(
        verbose_name=_('The source of information about '\
                       'Cinema Perpetuum Mobile'),
        choices=BACKLINKS
    )

    director = models.CharField(verbose_name=_('Director'),
                                max_length=1000)
    director_address = models.TextField(verbose_name=_('Director\'s address'))
    director_email = models.CharField(verbose_name=_('Director\'s email'),
                                      max_length=1000)
    director_site = models.CharField(verbose_name=_('Director\'s website'),
                                      max_length=1000, blank=True)
    director_phone = models.CharField(
        verbose_name=_('Director\'s phone number'),
        max_length=1000, blank=True)

    producer = models.CharField(verbose_name=_('Producer'),
                                max_length=1000, blank=True)
    producer_address = models.TextField(
        verbose_name=_('Producer\'s address'), blank=True)
    producer_email = models.CharField(
        verbose_name=_('Producer\'s email'), max_length=1000, blank=True)
    producer_site = models.CharField(
        verbose_name=_('Producer\'s website'), max_length=1000, blank=True)
    producer_phone = models.CharField(
        verbose_name=_('Producer\'s phone number'),
        max_length=1000, blank=True)

    screenwriter = models.CharField(verbose_name=_('Screenwriter'),
                                    max_length=1000, blank=True)
    editor = models.CharField(verbose_name=_('Editor'),
                                 max_length=1000, blank=True)
    music = models.CharField(verbose_name=_('Composer'),
                                max_length=1000, blank=True)
    director_photography = models.CharField(
        verbose_name=_('Director of photography'),
        max_length=1000, blank=True)

    owner = models.CharField(
        verbose_name=_('Owner'), max_length=1000, blank=True)
    owner_address = models.TextField(
        verbose_name=_('Owner\'s address'), blank=True)
    owner_email = models.CharField(
        verbose_name=_('Owner\'s email'), max_length=1000, blank=True)
    owner_site = models.CharField(
        verbose_name=_('Owner\'s website'), max_length=1000, blank=True)
    owner_phone = models.CharField(
        verbose_name=_('Owner\'s phone number'), max_length=1000, blank=True)

    distributor = models.CharField(
        verbose_name=_('Distributor'), max_length=1000, blank=True)
    distributor_address = models.TextField(
        verbose_name=_('Distributor\'s address'), blank=True)
    distributor_email = models.CharField(
        verbose_name=_('Distributor\'s email'), max_length=1000, blank=True)
    distributor_site = models.CharField(
        verbose_name=_('Distributor\'s website'), max_length=1000, blank=True)
    distributor_phone = models.CharField(
        verbose_name=_('Distributor\'s phone number'),
        max_length=1000, blank=True)
    
    allow_tv = models.IntegerField(
        verbose_name=_('Allow usage in festival TV commercials'),
        choices=YESNO, default=1)
    allow_noncommercial = models.IntegerField(
        verbose_name=_('Allow non commercial screenings'),
        choices=YESNO, default=1)
    allow_network = models.IntegerField(
        verbose_name=_('Allow screenings at partner\'s festivals'),
        choices=YESNO, default=1)

    applicant = models.CharField(verbose_name=_('Applicant'),
                                max_length=1000)
    applicant_address = models.TextField(verbose_name=_('Applicant\'s address'))
    applicant_email = models.CharField(verbose_name=_('Applicant\'s email'),
                                      max_length=1000)
    applicant_site = models.CharField(verbose_name=_('Applicant\'s website'),
                                      max_length=1000, blank=True)
    applicant_phone = models.CharField(
        verbose_name=_('Applicant\'s phone number'),
        max_length=1000, blank=True)
    
    def __repr__(self):
        return '<Film %s>' % (self.title)

class NewsEntry(TranslatableModel):
    added_at = models.DateTimeField(auto_now_add=True)

    translations = TranslatedFields(
        title = models.CharField(verbose_name=_('Title'), max_length=100),
        short_text = models.TextField(verbose_name=_('Short text'), max_length=1000),
        text = models.TextField(verbose_name=_('Text'), max_length=1000),
    )

class Page(TranslatableModel):
    slug = models.SlugField(max_length=50)

    translations = TranslatedFields(
        title = models.CharField(verbose_name=_('Title'), max_length=100),
        text = models.TextField(verbose_name=_('Text')),
    )
