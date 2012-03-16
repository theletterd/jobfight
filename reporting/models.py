from django.db import models
from django.contrib.auth.models import User

class Requisition(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class StatusValue(models.Model):
    status = models.ForeignKey(Status)
    user = models.ForeignKey(User)
    req = models.ForeignKey(Requisition)
    date = models.DateField()
    value = models.IntegerField()

    def __unicode__(self):
        return '%s - %s %s %s - %s' % (self.user.username, self.status.name, self.value, self.req.name, self.date.strftime('%Y-%m-%d'))

class UserProfile(models.Model):
    requisitions = models.ManyToManyField(Requisition, related_name="user_profiles")
    user = models.ForeignKey(User, unique=True)

    def __unicode__(self):
        return self.user.username
