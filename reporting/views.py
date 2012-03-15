from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    return render_to_response(
        'reporting/homepage.html',
        dict(message='butts'),
        context_instance=RequestContext(request)
    )

@login_required
def report(request):
    return render_to_response(
        'reporting/report.html',
        dict(message='wang'),
        context_instance=RequestContext(request)
    )
