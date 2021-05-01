from django.db import models
from datetime import datetime
from hotels.models import Hotel
from position.models import Position


class Staff(models.Model):

    id = models.AutoField(primary_key=True)

    fname = models.CharField(max_length=200, null=False)
    lname = models.CharField(max_length=200, null=False)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True) 
    security_level = models.CharField(max_length=200) 
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, default='Male')
    is_eom = models.BooleanField(default=False)# employee of the month
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    # Foreign Fields 
    
    hotel_id = models.ForeignKey(Hotel, on_delete=models.DO_NOTHING)
    job_title = models.ForeignKey(Position , on_delete=models.DO_NOTHING)
    


    def __str__(self):
        return self.id