import datetime

from collections import defaultdict
from functools import partial

from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from forms import StatusValueForm

from reporting.constants import ReportDataType, ReportRangeType
from reporting import logic
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

    users = User.objects.all()
    reqs = user.get_profile().requisitions.all()
    statuses = models.Status.objects.all().order_by()

    status_values = models.StatusValue.objects.all()
    user_status_matrix = logic.get_matrix(ReportDataType.USER_STATUS, ReportRangeType.THIS_WEEK)
    req_status_matrix = logic.get_matrix(ReportDataType.REC_STATUS, ReportRangeType.THIS_WEEK, user__id__exact=user.id)

    return render_to_response(
        'reporting/report.html',
        dict(
			user=user,
			users=users,
			reqs=reqs,
            statuses=statuses,

            user_status_matrix=user_status_matrix,
            req_status_matrix=req_status_matrix,
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

@login_required
@csrf_exempt
def new_status_value(request):
    if request.method != "POST":
        return redirect('/reporting/report')
    post_data = request.POST
    print post_data
    user = request.user
    status = models.Status.objects.get(id=post_data['status_id'])
    req = models.Requisition.objects.get(id=post_data['req_id'])

    print status
    print req
    value = post_data['value']


    status_value = models.StatusValue(user=user, req=req, status=status, value=value, date=datetime.date.today())

    status_value.save()
    return redirect('/reporting/report')
