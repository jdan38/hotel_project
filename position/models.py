from django.db import models



class Position(models.Model):
    
    job_title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    level = models.CharField(max_length=200)
    job_description = models.TextField(blank=True)
    payrate = models.IntegerField()# how much employee gets paid
    paytype = models.CharField(max_length=20)# hourly or salary


    def __str__(self):
        return self.job_title