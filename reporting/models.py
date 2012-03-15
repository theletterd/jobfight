from django.db import models
from django.contrib.auth.models import User


class Metric(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class MetricValue(models.Model):
    metric = models.ForeignKey(Metric)
    user = models.ForeignKey(User)
    date = models.DateField()
    value = models.IntegerField()

    def __unicode__(self):
        nice_date = self.date
        return '%s - %s %s - %s' % (self.user.username, self.metric.name, self.value, self.date.strftime('%Y-%m-%d'))
