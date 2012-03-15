from collections import defaultdict
from functools import partial

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from forms import StatusValueForm

from reporting import models

def home(request):
    return render_to_response(
        'reporting/homepage.html',
        dict(message='Dingleberries!'),
        context_instance=RequestContext(request)
    )

@login_required
def report(request):
    #user = request.user
    users = User.objects.all()

    statuses = models.Status.objects.all().order_by("name")

    #status_values = models.StatusValue.objects.filter(user=user)
    status_values = models.StatusValue.objects.all()

    status_values_by_req_id = {}
    for status_value in status_values:
        status_values_by_req_id.setdefault(status_value.req.id, []).append(status_value)

    status_values_by_user_id = {}
    user_status_matrix = defaultdict(partial(defaultdict, int))
    for status_value in status_values:
        status_values_by_user_id.setdefault(status_value.user.id, []).append(status_value)
        user_status_matrix[status_value.user.id][status_value.status.id] += 1

    return render_to_response(
        'reporting/report.html',
        dict(
            statuses=statuses,
            user_status_matrix=user_status_matrix,
            status_values_by_user_id=status_values_by_user_id,
            status_values_by_req_id=status_values_by_req_id,
        ),
        context_instance=RequestContext(request)
    )


@login_required
def add_status_value(request):

    template = 'reporting/add_status_value.html'

    if request.method == "GET":
        status_value_form = StatusValueForm(request.user)
        return render_to_response(
            template,
            dict(form=status_value_form),
            context_instance=RequestContext(request)
        )
    elif request.method == "POST":
        status_value_form = StatusValueForm(request.user, request.POST)
        if not status_value_form.errors:
            status_value = status_value_form.save(commit=False)
            status_value.user = request.user
            status_value.save()

            return redirect('/reporting/report')
        else:
            return render_to_response(
                template,
                dict(form=status_value_form),
                context_instance=RequestContext(request)
            )
