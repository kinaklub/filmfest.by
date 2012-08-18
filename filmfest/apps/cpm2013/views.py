from django.http import HttpResponse
from django.views.generic.create_update import create_object
from django.shortcuts import render_to_response
from django.template import RequestContext

from apps.cpm2013.models import Submission, NewsEntry
from apps.cpm2013.forms import SubmissionForm

def index(request):
    news = NewsEntry.objects.language().order_by('-added_at')[:10]
    return render_to_response(
        'cpm2013/index.html',
        {'news': news},
        context_instance=RequestContext(request),
    )

def submit(request):
    return create_object(
        request, model=Submission, form_class=SubmissionForm,
        template_name='cpm2013/submit.html'
    )

def rules(request):
    return render_to_response('cpm2013/rules.html')


from django_xhtml2pdf.utils import generate_pdf

def test(request):
    template_name = 'cpm2013/pdf/submission.html'
    context = {}

    resp = HttpResponse(content_type='application/pdf')

    from django.template.loader import get_template
    from django.template.context import Context

    tmpl = get_template(template_name)
    html = tmpl.render(Context(context))

    from xhtml2pdf import pisa
    pisa.pisaDocument(html.encode("utf-8"), resp , encoding='utf-8')
    
    return resp

