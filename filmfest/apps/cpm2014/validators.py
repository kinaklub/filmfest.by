from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

def validate_checked(value):
    if not value:
        raise ValidationError(_('Please check if you agree'))
