from django.db import models
from datetime import datetime
from staffs.models import Staff
from hotels.models import Hotel

class Listing(models.Model):
    id = models.ForeignKey(Staff, related_name='staff_id', on_delete=models.DO_NOTHING)
    id = models.ForeignKey(Hotel, related_name='hotel_id', on_delete=models.DO_NOTHING)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    roomnumber = models.CharField(max_length=200)
    address = models.ForeignKey(Hotel, related_name='hotel_address', on_delete=models.DO_NOTHING)
    city = models.ForeignKey(Hotel, related_name='hotel_city', on_delete=models.DO_NOTHING)
    state = models.ForeignKey(Hotel, related_name='hotel_state', on_delete=models.DO_NOTHING)
    zipcode = models.ForeignKey(Hotel, related_name='hotel_zipcode', on_delete=models.DO_NOTHING)
    description = models.TextField(blank=True)
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