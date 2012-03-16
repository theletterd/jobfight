from datetime import date
from datetime import datetime

from collections import defaultdict
from functools import partial

from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext

from reporting.constants import Resolution, ReportDataType, ReportRangeType
from reporting.forms import ReportTypeForm, StatusValueForm
from reporting import logic
from reporting import models
from reporting import timeutil

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

    default_report_type = 'THIS_WEEK'
    report_range_type = getattr(ReportRangeType, default_report_type)

    # I tried to avoid handling POSTs here, but it was late and I was tired
    if request.method == 'POST':
        report_type_form = ReportTypeForm(request.POST)
        if report_type_form.is_valid():
            report_range_type = report_type_form.cleaned_data['report_type']
    else:
        report_type_form = ReportTypeForm(dict(report_type=default_report_type))

    edit_date = timeutil.default_today()
    if report_range_type['resolution'] == Resolution.WEEKLY:
        start_date, end_date = logic.range_from_report_range_type(report_range_type)
        edit_date = logic.pick_day_from_week(start_date, end_date)

    user_status_matrix = logic.get_matrix(ReportDataType.USER_STATUS, report_range_type)
    req_status_matrix = logic.get_matrix(ReportDataType.REC_STATUS, report_range_type, user__id__exact=user.id)

    return render_to_response(
        'reporting/report.html',
        dict(
			user=user,
			users=users,
			reqs=reqs,
            statuses=statuses,

            user_status_matrix=user_status_matrix,
            req_status_matrix=req_status_matrix,

            edit_date=edit_date,
            report_type_form=report_type_form,
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
    user = request.user

    status = models.Status.objects.get(id=post_data['status_id'])
    req = models.Requisition.objects.get(id=post_data['req_id'])
    edit_date = datetime.strptime(post_data['edit_date'], "%Y-%m-%d").date()

    value = post_data['value']

    status_value = models.StatusValue(user=user, req=req, status=status, value=value, date=edit_date)

    status_value.save()
    return redirect('/reporting/report')
