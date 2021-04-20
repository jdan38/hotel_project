from django.db import models
from datetime import datetime

from hotels.models import Hotel

class Listing(models.Model):
    
    # hotel_id = models.ForeignKey(Hotel, related_name='hotel_id', on_delete=models.DO_NOTHING)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.DO_NOTHING, default='0')
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    roomnumber = models.CharField(max_length=200)
   
    price = models.IntegerField()
    beds = models.IntegerField()
    occupancy = models.IntegerField()
    is_occupied = models.BooleanField(default=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    bathroom = models.ImageField(upload_to='photos/%Y/%m/%d/')
    tv = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    date_in = models.DateTimeField(default=datetime.now, blank=True)
    date_out = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.roomnumber