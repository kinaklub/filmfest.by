from django.utils import translation
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _
from django.db import models

from hvad.models import TranslatableModel, TranslatedFields

from submissions.constants import SECTIONS, TRANSLATION_LANGUAGES
from submissions.models import Submission


class Program(models.Model):
    code = models.SlugField(
        unique=True, verbose_name=_(u'Code'),
        help_text=_(u'Unique technical code, e.g. regional_mogilev')
    )
    section = models.IntegerField(choices=SECTIONS, verbose_name=_(u'Section'))
    __unicode__ = lambda self: self.code

    @cached_property
    def translation(self):
        try:
            return ProgramTranslation.objects.get(
                program=self, language=translation.get_language()
            )
        except ProgramTranslation.DoesNotExist:
            return None


class ProgramTranslation(models.Model):
    program = models.ForeignKey(Program)
    language = models.CharField(max_length=2, choices=TRANSLATION_LANGUAGES)
    name = models.CharField(verbose_name=_(u'Name'), max_length=1000)
    description = models.CharField(verbose_name=_(u'Description'),
                                   max_length=1000)

    class Meta:
        unique_together = [('language', 'program')]


class SubmissionScreening(models.Model):
    num = models.IntegerField()
    submission = models.ForeignKey(Submission)
    program = models.ForeignKey(Program)

    class Meta:
        unique_together = [('submission', 'program')]


class City(TranslatableModel):
    code = models.CharField(verbose_name=_(u'Code'), max_length=1000)
    priority = models.IntegerField(verbose_name=_(u'Priority'))

    translations = TranslatedFields(
        name = models.CharField(verbose_name=_(u'Name'), max_length=1000)
    )

    __unicode__ = lambda self: self.code

    class Meta:
        verbose_name_plural = 'Cities'


class Place(TranslatableModel):
    code = models.CharField(verbose_name=_(u'Code'), max_length=1000)
    city = models.ForeignKey(City)

    translations = TranslatedFields(
        name = models.CharField(verbose_name=_(u'Name'), max_length=1000),
        address = models.CharField(verbose_name=_(u'Address'), max_length=1000)
    )

    __unicode__ = lambda self: self.code


class Event(TranslatableModel):
    code = models.CharField(verbose_name=_(u'Code'), max_length=1000)
    starts_at = models.DateTimeField(verbose_name=_('Starts at'), db_index=True)
    place = models.ForeignKey(Place)
    program = models.ForeignKey(Program, null=True, blank=True)

    translations = TranslatedFields(
        name = models.CharField(verbose_name=_(u'Name'), max_length=1000),
        description = models.TextField(verbose_name=_('Description'),
                                       blank=True, null=True)
    )

    __unicode__ = lambda self: self.code
