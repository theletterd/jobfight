from django.db import models
from django.contrib.auth.models import User

REQ_TYPE = (
    (0, "Engineeering"),
    (1, "New Grad"),
    (2, "Summer Intern"),
    (3, "Back-end"),
    (4, "Eng Manager"),
    (5, "Mobile"),
    (6, "Search"),
    (7, "Ads/Revenue"),
    (8, "Front-end"),
    (9, "Web Dev"),
    (10, "Product/Design"),
    (11, "PM - Consumer"),
    (12, "PM - Local Business"),
    (13, "PM - International"),
    (14, "PM - New Grad"),
    (15, "PM Intern Summer"),
    (16, "UI Designer"),
    (17, "UI Designer - New Grad"),
    (18, "UI Designer Intern"),
    (19, "Systems/IT"),
    (20, "Sys Infra Developer"),
    (21, "Release Eng"),
    (22, "Sys Admin (Corp)"),
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
