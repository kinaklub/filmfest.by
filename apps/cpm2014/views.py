
# -*- coding: utf-8 -*-
import io
import json
import os.path
from collections import defaultdict

from django.contrib.admin.views.decorators import staff_member_required
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import (
    get_object_or_404, render_to_response, redirect, redirect
)
from django.template import RequestContext
from django.utils import translation
from django.utils.translation import ugettext_lazy as _
from django.views.generic.base import RedirectView
from django.conf import settings

from apps.cpm2014.constants import APP_ROOT, TRANSLATION_LANGUAGES
from apps.cpm2014.models import (
    Event, NewsEntry, Program, ProgramTranslation,
    Submission, SubmissionScreening, SubmissionTranslation
)
from apps.cpm2014.forms import (
    ProgramForm, ProgramTranslationForm,
    SubmissionForm, SubmissionTranslationForm
)
from apps.cpm2014.tasks import SendSubmissionEmail


class IndexView(RedirectView):
    url = '/'
    permanent = False
index = IndexView.as_view()

def submit(request):
    form = SubmissionForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        submission = form.save(commit=False)
        submission.submission_language = translation.get_language()
        submission.save()

        SendSubmissionEmail().apply_async(args=[submission])

        return render_to_response(
            'cpm2014/submit_done.html',
            {'email': submission.applicant_email},
            context_instance=RequestContext(request),
        )

    return render_to_response(
        'cpm2014/submit.html',
        {'form': form},
        context_instance=RequestContext(request),
    )


class Rules:
    LANGUAGES = {
        'be': 'rules_ru.md',
        'ru': 'rules_ru.md',
        'en': 'rules_en.md',

    }
    RTL = set(('ar',))

    PATH = os.path.join(APP_ROOT, 'docs')

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
            'cpm2014/rules.html',
            {
                'rules': rules,
                'rtl': rtl,
                'current_lang': lang,
                'languages': sorted(self.LANGUAGES.iterkeys()),
            },
            context_instance=RequestContext(request),
        )
rules = Rules()

def partners(request):
    img_dir = '/static/cpm2014/banners/'
    banners = [
        (
            img_dir + 'where.png',
            'http://www.spn.ru/publishing/whereminsk/',
            'Where Minsk'
        ),
        (
            img_dir + 'relax.png',
            'http://relax.by/',
            'relax.by - развлечения в Минске, развлекательные центры столицы'
        ),

        (
            img_dir + 'minsk24dok.png',
            'http://mtis.tv/',
            'Минск 24 ДОК'
        ),
        (
            img_dir + 'nomadic.png',
            'http://vagrant.kinaklub.org/',
            'Nomadic Film Club'
        ),
        (
            img_dir + 'filmschool.png',
            'http://filmschool.by/',
            'Минская Киношкола-студия'
        ),
        (
            img_dir + 'citydog.png',
            'http://citydog.by/',
            'citydog.by - журнал о Минске'
        ),
        (
            img_dir + 'kultprosvet.png',
            'http://kultprosvet.by/',
            'Культпросвет – интернет-журнал о театрах и синтетических видах искусства'
        ),
        (
            img_dir + 'n_europe.png',
            'http://n-europe.eu/',
            'Журнал для тех, кто думает по-европейски'
        ),
        (
            img_dir + 'cinemahall.png',
            'http://cinemahall.org/',
            'cinemahall.org'
        ),
        (
            img_dir + 'tokino.png',
            'http://tokino.lt/',
            'Беларуско-литовский фестиваль небюджетного кино и видео «toKino»'
        ),
        (
            img_dir + 'makeout.png',
            'http://makeout.by/',
            'MAKEOUT — часопіс пра гендар, сэксуальнасць і асаблівасці іх праяваў у Беларусі'
        ),
        (
            img_dir + 'talaka.png',
            'http://talaka.by/',
            'Talaka.by – некоммерческая платформа, которая помогает активным людям в Беларуси реализовывать значимые для общества проекты'
        ),
        (
            img_dir + 'minchane.png',
            'http://minchane.by/',
            'Минчане'
        ),
        (
            img_dir + 'generationby.png',
            'http://generation.by/',
            'Generation.by — інфармацыйны рэсурс пра жыццё і прыгоды беларускага пакалення Y, маладых людзей, якія нарадзіліся ў 80-90 г.г. XX стагоддзя'
        ),
        (
            img_dir + '34.png',
            'http://34mag.net/',
            '34mag.net – моладзевы часопіс пра актуальнае і цікавае ў Беларусі і свеце'
        ),
        (
            img_dir + 'moviesthatmatter.png',
            'http://www.moviesthatmatter.nl/',
            'Movies That Matter'
        ),
        (
            img_dir + 'eksperiment.png',
            'http://md-eksperiment.org/',
            'md-eksperiment.org'
        ),
        (
            img_dir + 'cinewest.png',
            'http://www.cinewest.org/',
            'Cinewest'
        ),
        (
            img_dir + '100second.png',
            'http://100fest.com/pages/en/',
            'International 100 Seconds Film Festival'
        ),
        (
            img_dir + 'videomaker.png',
            'http://www.videomakerfilmfestival.com/',
            'VideoMaker Film Festival'
        ),
    ]
    return render_to_response(
        'cpm2014/partners.html',
        {'banners': banners},
        context_instance=RequestContext(request),
    )


def press_kit(request):
    return render_to_response(
        'cpm2014/press_kit.html', {},
        context_instance=RequestContext(request),
    )


@staff_member_required
def translation_details(request, submission_id, lang):
    submission = get_object_or_404(Submission, id=submission_id)
    translation, created = SubmissionTranslation.objects.get_or_create(
        submission=submission, language=lang
    )

    data = [
        (_(u'Title'), submission.title, translation.title),
        (_(u'Director'), submission.director, translation.director),
        (_(u'Genre'), submission.genre, translation.genre),
        (_(u'Synopsis'), submission.synopsis, translation.synopsis),
        (_(u'Synopsis (short)'), '', translation.synopsis_short),
    ]
    context = {'submission': submission, 'data': data, 'lang': lang}
    return render_to_response('cpm2014/translation_details.html', context,
                              context_instance=RequestContext(request))


@staff_member_required
def translation_edit(request, submission_id, lang):
    submission = get_object_or_404(Submission, id=submission_id)
    translation, created = SubmissionTranslation.objects.get_or_create(
        submission=submission, language=lang
    )
    form = SubmissionTranslationForm(
        request.POST or None, instance=translation
    )

    if form.is_valid():
        form.save()
        return redirect('cpm2014:translation_details', submission_id, lang)

    context = {
        'submission': submission,
        'translation': translation,
        'form': form,
        'lang': lang
    }
    return render_to_response('cpm2014/translation_edit.html', context,
                              context_instance=RequestContext(request))


@staff_member_required
def translations_all_json(request):
    response_dict = defaultdict(dict)

    for t in SubmissionTranslation.objects.all().select_related('submission'):
        translation.activate(t.language)

        response_dict[t.submission_id][t.language] = {
            'title': t.title,
            'genre': t.genre,
            'synopsis': t.synopsis,
            'synopsis_short': t.synopsis_short,
            'director': t.director,
            'language': t.submission.get_language_display(),
        }

    translation.deactivate()

    return HttpResponse(
        json.dumps(response_dict, indent=2),
        content_type="application/json"
    )
