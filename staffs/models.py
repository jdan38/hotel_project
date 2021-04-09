from django.db import models
from datetime import datetime
from hotels.models import Hotel


class Staff(models.Model):
    name = models.CharField(max_length=200)
    staff_id = models.AutoField(primary_key=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    hotel_id = models.ForeignKey(Hotel, on_delete=models.DO_NOTHING)
    
    jobtitle = models.CharField(max_length=200)
    level = models.CharField(max_length=200)
    job_description = models.TextField(blank=True)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    is_eom = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    payrate = models.IntegerField()
    paytype = models.CharField(max_length=20)


    def __str__(self):
        return self.name