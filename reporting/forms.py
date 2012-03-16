from django import forms
from django.forms import ModelForm
from models import StatusValue, Requisition

import datetime

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
