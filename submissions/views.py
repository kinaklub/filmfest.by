from collections import defaultdict
import json

from django.contrib.admin.views.decorators import staff_member_required
from django.template import RequestContext
from django.http import HttpResponse
from django.utils import translation
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404, render_to_response, redirect

from submissions.forms import SubmissionForm, SubmissionTranslationForm
from submissions.models import Submission, SubmissionTranslation
from submissions.tasks import SendSubmissionEmail


__all__ = ['submit']


def submit(request):
    form = SubmissionForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        submission = form.save(commit=False)
        submission.submission_language = translation.get_language()
        submission.save()

        SendSubmissionEmail().apply_async(args=[submission])

        return render_to_response(
            'submissions/submit_done.html',
            {'email': submission.applicant_email},
            context_instance=RequestContext(request),
        )

    return render_to_response(
        'submissions/submit.html',
        {'form': form},
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
    return render_to_response('submissions/translation_details.html', context,
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
        return redirect('submissions_translation_details', submission_id, lang)

    context = {
        'submission': submission,
        'translation': translation,
        'form': form,
        'lang': lang
    }
    return render_to_response('submissions/translation_edit.html', context,
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
