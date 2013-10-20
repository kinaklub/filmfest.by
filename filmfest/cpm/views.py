from django.http import HttpResponseForbidden
from django.shortcuts import render_to_response
from django.template import RequestContext


def angular(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    return render_to_response(
        'cpm/angular.html', {}, context_instance=RequestContext(request)
    )
