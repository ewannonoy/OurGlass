from django.db import models
from datetime import date, time
# Create your models here.

class UserSked(models.Model):
    title = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateField(default = date.today, blank=True)
    ratings = models.IntegerField(default = 0,null=True, blank=True)
    likes = models.IntegerField(default = 0,blank = True, null = True)

    def __unicode__(self):
        return '%s' % (self.title)
