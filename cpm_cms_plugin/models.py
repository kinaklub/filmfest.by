from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from django.db import models

class ContactPluginModel(CMSPlugin):
    contact_name = models.CharField(verbose_name=_(u'Contact Name'),
                                    max_length = 50)
    contact_phone = models.CharField(verbose_name=_(u'Phone Number'),
                                     max_length = 50)
    contact_email = models.EmailField(verbose_name=_(u'Email'),
                                      max_length = 100)
    contact_skype = models.CharField(verbose_name=_(u'Skype'),
                                     max_length = 50)
    additional_info = models.CharField(verbose_name = _(u'Additional Info'),
                                       max_length = 50)
