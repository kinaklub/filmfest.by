from django import forms
from django.utils.translation import ugettext_lazy as _


class FesthomeImportForm(forms.Form):
    document = forms.FileField()#verbose_name=_(u'Document'))
