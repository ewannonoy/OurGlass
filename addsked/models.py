from django.db import models
from datetime import date, time, datetime
# Create your models here.

class UserSked(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    event_date = models.DateField(default = date.today, blank=True)
    event_time = models.TimeField(default = datetime.now, auto_now=False, auto_now_add=False,blank=True)    
    date_created = models.DateField(default = date.today, null=True, blank=True)
    ratings = models.IntegerField(default = 0,null=True, blank=True)
    likes = models.IntegerField(default = 0,blank = True, null = True)
    photo = models.ImageField(upload_to = 'OurGlass/media/images/events/', null=True, default = 'OurGlass/media/images/events/default/default.png')

    def __unicode__(self):
        return '%s' % (self.title)
