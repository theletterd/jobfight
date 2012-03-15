from django.contrib.auth.decorators import login_required
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


@login_required
def add_status_value(request):

    template = 'reporting/add_status_value.html'

    if request.method == "GET":
        status_value_form = StatusValueForm()
        return render_to_response(
            template,
            dict(form=status_value_form),
            context_instance=RequestContext(request)
        )
    elif request.method == "POST":
        status_value_form = StatusValueForm(request.POST)
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
