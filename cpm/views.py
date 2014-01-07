from django.http import HttpResponseForbidden
from django.shortcuts import render_to_response
from django.template import RequestContext

from cpm.forms import ScreeningPlaceProposalForm


def angular(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    return render_to_response(
        'cpm/angular.html', {}, context_instance=RequestContext(request)
    )


def new_screening_place(request):
    form = ScreeningPlaceProposalForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render_to_response(
            'cpm/new_screening_place_done.html',
            {'form': form},
            context_instance=RequestContext(request)
        )
    return render_to_response(
        'cpm/new_screening_place.html',
        {'form': form},
        context_instance=RequestContext(request)
    )
