from django import forms
from django.forms import ModelForm
from models import StatusValue

import datetime

class StatusValueForm(ModelForm):

    date = forms.DateField(
        initial=datetime.datetime.today().strftime('%m/%d/%Y')
    )

    class Meta:
        model = StatusValue
        exclude = ('user')
