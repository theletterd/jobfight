from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

from reporting import models

def home(request):
    return render_to_response(
        'reporting/homepage.html',
        dict(message='butts'),
        context_instance=RequestContext(request)
    )

@login_required
def report(request):
    user = request.user

    status_values = models.StatusValue.objects.filter(user=user)

    status_values_by_req_id = {}
    for status_value in status_values:
        status_values_by_req_id.setdefault(status_value.req.id, []).append(status_value)


    return render_to_response(
        'reporting/report.html',
        dict(
            user=user,
        ),
        context_instance=RequestContext(request)
    )
