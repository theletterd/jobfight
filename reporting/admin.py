from models import Requisition, Status, StatusValue, UserProfile
from django.contrib.auth.models import User
from django.contrib import admin

admin.site.register(Requisition)
admin.site.register(Status)
admin.site.register(StatusValue)
admin.site.register(UserProfile)
