import datetime
from functools import partial

from django import forms
from django.forms import ModelForm
from reporting.constants import ReportRangeType
from reporting.models import StatusValue, Requisition
from reporting import textutil

class StatusValueForm(ModelForm):

    date = forms.DateField(
        initial=datetime.datetime.today().strftime('%m/%d/%Y')
    )

    class Meta:
        model = StatusValue
        exclude = ('user')

    def  __init__(self, user, *args, **kwargs):
        super(StatusValueForm, self).__init__(*args, **kwargs)
        profile = user.get_profile()
        req_choices = profile.requisitions.values_list('id', 'name')
        self.fields['req'].choices = req_choices

class ReportType(forms.Form):
    report_type = forms.TypedChoiceField(
            coerce=partial(getattr, ReportRangeType),
            empty_value=None,
            choices=dict((type, textutil.title_case_var(type)) for type in ReportRangeType.all_types()),
    )
