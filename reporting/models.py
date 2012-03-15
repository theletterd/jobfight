from django.db import models
from django.contrib.auth.models import User

REQ_TYPE = (
        (0, 'Intern'),
        (1, 'Developer'),
        (2, 'PM'),
)

class Status(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class StatusValue(models.Model):
    status = models.ForeignKey(Status)
    user = models.ForeignKey(User)
    date = models.DateField()
    req = models.IntegerField(choices=REQ_TYPE)
    value = models.IntegerField()

    def __unicode__(self):
        nice_date = self.date
        return '%s - %s %s - %s' % (self.user.username, self.status.name, self.value, self.date.strftime('%Y-%m-%d'))
