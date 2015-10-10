#!/usr/bin/env python
import os
import sys


def fix_django_cms_3193():
    if sys.argv[1] == 'loaddata':
        from django.db.models import signals
        from cms.models import Page
        from cms.signals import update_placeholders
        signals.post_save.disconnect(update_placeholders, sender=Page)


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "filmfest.settings")
    from django.core.management import execute_from_command_line
    fix_django_cms_3193()
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
