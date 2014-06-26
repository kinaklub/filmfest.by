
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
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import RedirectView
from django.conf import settings

from rest_framework import viewsets

from apps.cpm2014.constants import APP_ROOT, TRANSLATION_LANGUAGES
from apps.cpm2014.models import (
    Event, NewsEntry, Program, ProgramTranslation,
    Submission, SubmissionScreening, SubmissionTranslation
)
from apps.cpm2014.forms import (
    ProgramForm, ProgramTranslationForm,
    SubmissionForm, SubmissionTranslationForm
)
from apps.cpm2014.serializers import SubmissionSerializer
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
            img_dir + 'maysternia.png',
            None,
            'Творческий центр "Майстэрня"'
        ),
        (
            img_dir + 'moviesthatmatter.png',
            'http://www.moviesthatmatter.nl/',
            'Movies That Matter'
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



class SubmissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows submissions to be viewed or edited.
    """
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

    @csrf_exempt
    def create(self, request, *args, **kwargs):
        return super(SubmissionViewSet, self).create(request, *args, **kwargs)

    @csrf_exempt
    def update(self, request, *args, **kwargs):
        return super(SubmissionViewSet, self).update(request, *args, **kwargs)

    get_paginate_by = lambda self: None


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


@staff_member_required
def program_list(request):
    programs = Program.objects.all().order_by('id')
    programs = programs.prefetch_related()

    context = {'programs': programs}
    return render_to_response('cpm2014/program_list.html', context,
                              context_instance=RequestContext(request))


def program_details(request, program_id):
    program = get_object_or_404(Program, id=program_id)
    try:
        trans = ProgramTranslation.objects.get(
            language=translation.get_language(), program=program
        )
    except ProgramTranslation.DoesNotExist:
        trans = None
    screenings_qs = program.submissionscreening_set.all()
    screenings_qs = screenings_qs.select_related()
    screenings_qs = screenings_qs.prefetch_related('submission__submissiontranslation_set')

    context = {
        'program': program,
        'translation': trans,
        'screenings': sorted(
            screenings_qs,
            key=lambda screening: screening.num
        ),
        'editable': request.user.is_staff
    }
    return render_to_response('cpm2014/program_details.html', context,
                              context_instance=RequestContext(request))


@staff_member_required
@transaction.commit_on_success
def program_edit(request, program_id=None):
    if program_id is None:
        program = Program()
        translations = [
            ProgramTranslation(
                language=lang
            ) for lang, lang_name in TRANSLATION_LANGUAGES
        ]
    else:
        program = get_object_or_404(Program, id=program_id)
        translations = [
            ProgramTranslation.objects.get_or_create(
                language=lang, program=program
            )[0] for lang, lang_name in TRANSLATION_LANGUAGES
        ]

    films_initial = '\n'.join(
        str(scr.submission_id) for scr in program.submissionscreening_set.all()
    )
    form = ProgramForm(request.POST or None, instance=program,
                       initial={'films': films_initial})

    translation_forms = [
        ProgramTranslationForm(
            request.POST or None,
            instance=trans,
            prefix=trans.language
        ) for trans in translations
    ]

    if form.is_valid() and all(f.is_valid() for f in translation_forms):
        program = form.save(commit=False)
        program.save()

        SubmissionScreening.objects.filter(program=program).delete()
        SubmissionScreening.objects.bulk_create(
            [
                SubmissionScreening(
                    num=index,
                    submission=submission,
                    program=program
                )
                for index, submission in enumerate(
                    form.cleaned_data['films'], 1
                )
            ]
        )

        for translation_form in translation_forms:
            trans = translation_form.save(commit=False)
            trans.program = program
            trans.save()

        return redirect('cpm2014:program_details', program_id=program.id)

    context = {
        'program': program,
        'form': form,
        'translation_forms': translation_forms
    }
    return render_to_response('cpm2014/program_edit.html', context,
                              context_instance=RequestContext(request))


def event_details(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if event.program:
        screenings_qs = event.program.submissionscreening_set.all()
        screenings_qs = screenings_qs.select_related()
        screenings_qs = screenings_qs.prefetch_related(
            'submission__submissiontranslation_set'
        )
    else:
        screenings_qs = SubmissionScreening.objects.none()

    context = {
        'event': event,
        'screenings': sorted(
            screenings_qs,
            key=lambda screening: screening.num
        ),
    }
    return render_to_response('cpm2014/event_details.html', context,
                              context_instance=RequestContext(request))
