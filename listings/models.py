from django.db import models
from datetime import datetime

from hotels.models import Hotel

class Listing(models.Model):
    
    
    hotel_id = models.ForeignKey(Hotel, on_delete=models.DO_NOTHING, default='1')
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    roomnumber = models.CharField(max_length=20)
    price = models.IntegerField()
    
    beds = models.CharField(max_length=20, default='1')

    bed_size = models.CharField(max_length=20, default='single')
    occupancy = models.IntegerField()
    
    description = models.CharField(max_length=200, default='pool')
    is_occupied = models.BooleanField(default=False)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    bathroom = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    tv = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    date_in = models.DateTimeField(default=datetime.now, blank=True)
    date_out = models.DateTimeField(default=datetime.now, blank=True)

    def __int__(self):
        return self.id
        