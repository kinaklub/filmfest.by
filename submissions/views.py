from django.template import RequestContext
from django.utils import translation
from django.shortcuts import render_to_response

from submissions.forms import SubmissionForm
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
