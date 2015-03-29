from django.contrib.admin.views.decorators import staff_member_required
from django.db import transaction
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.utils import translation

from submissions.constants import TRANSLATION_LANGUAGES
from events.models import Event, Program, ProgramTranslation,\
     SubmissionScreening
from events.forms import ProgramForm, ProgramTranslationForm     


@staff_member_required
def program_list(request):
    programs = Program.objects.all().order_by('id')
    programs = programs.prefetch_related()

    context = {'programs': programs}
    return render_to_response('events/program_list.html', context,
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
    return render_to_response('events/program_details.html', context,
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

        return redirect('events_program_details', program_id=program.id)

    context = {
        'program': program,
        'form': form,
        'translation_forms': translation_forms
    }
    return render_to_response('events/program_edit.html', context,
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
    return render_to_response('events/event_details.html', context,
                              context_instance=RequestContext(request))
# Create your views here.
