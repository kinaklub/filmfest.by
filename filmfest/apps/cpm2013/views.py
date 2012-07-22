from django.http import HttpResponse
from django.views.generic.create_update import create_object
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Submission
from forms import SubmissionForm

def index(request):
    return render_to_response(
        'cpm2013/index.html',
        context_instance=RequestContext(request),
    )

def submit(request):
    return create_object(
        request, model=Submission, form_class=SubmissionForm,
        template_name='cpm2013/submit.html'
    )

def rules(request):
    return render_to_response('cpm2013/rules.html')