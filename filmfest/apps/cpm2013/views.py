import io
import os
import os.path
from tex import latex2pdf

from django.http import HttpResponse
from django.views.generic.create_update import create_object
from django.shortcuts import render_to_response, get_object_or_404
from django.template import loader, RequestContext
from django.utils import translation
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from apps.cpm2013.models import Submission, NewsEntry, Page
from apps.cpm2013.forms import SubmissionForm
from apps.cpm2013.tasks import SendSubmissionEmail

def index(request):
    news = NewsEntry.objects.language().order_by('-added_at')[:10]
    return render_to_response(
        'cpm2013/index.html',
        {'news': news},
        context_instance=RequestContext(request),
    )

def submit(request):
    form = SubmissionForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        submission = form.save(commit=False)
        submission.submission_language = translation.get_language()
        submission.save()

        SendSubmissionEmail().apply_async(args=[submission])
        
        return render_to_response(
            'cpm2013/submit_done.html',
            {'email': submission.applicant_email},
            context_instance=RequestContext(request),
        )
        
    return render_to_response(
        'cpm2013/submit.html',
        {'form': form},
        context_instance=RequestContext(request),
    )

def page(request, slug):
    base_page = get_object_or_404(Page, slug=slug)
    pages = base_page._meta.translations_model.objects.all()
    pages = dict((t.language_code, t) for t in pages)

    current_lang = translation.get_language()
    if current_lang in pages:
        page = pages[current_lang]
    else:
        for lang_code in ['en', 'ru', 'be']:
            if lang_code in pages:
                page = pages[lang_code]
                break

    return render_to_response(
        'cpm2013/page.html',
        {'page': page},
        context_instance=RequestContext(request),
    )

class Rules:
    LANGUAGES = {
        'be': 'rules_ru.md',
        'ru': 'rules_ru.md',
        'en': 'rules_en.md',

        'ar': 'rules_ar.md',
        'cn': 'rules_cn.md',
        'de': 'rules_de.md',
        'es': 'rules_es.md',
        'fr': 'rules_fr.md',
        'it': 'rules_it.md',
        'pl': 'rules_pl.md',
        'pt': 'rules_pt.md',
    }
    RTL = set(('ar',))

    PATH = os.path.join(settings.PROJECT_ROOT, 'apps', 'cpm2013', 'docs')

    @classmethod
    def translation(cls, lang):
        if lang is None:
            lang = translation.get_language()

        lang = lang.lower()
        if lang not in cls.LANGUAGES:
            lang = 'en'

        rules = os.path.join(cls.PATH, cls.LANGUAGES[lang])
        rtl = lang in cls.RTL

        return lang, rules, rtl

    def __call__(self, request, lang=None):
        lang, rules_filename, rtl = self.translation(lang)
        rules = io.open(
            rules_filename,
            'r', encoding='utf-8'
        ).read()
        return render_to_response(
            'cpm2013/rules.html',
            {
                'rules': rules,
                'rtl': rtl,
                'current_lang': lang,
                'languages': sorted(self.LANGUAGES.iterkeys()),
            },
            context_instance=RequestContext(request),
        )
rules = Rules()