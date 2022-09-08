from asyncio.windows_events import NULL
from email.policy import default
from django.db import models



# Create your models here.
class Region(models.Model):
    region_name = models.CharField(max_length=100)
    def __str__(self):
        return self.region_name




class Restaurant(models.Model):
    Restaurant_name = models.CharField(max_length=40)
    region = models.ForeignKey(Region,on_delete=models.CASCADE,default=None,null=True)
    x = models.FloatField()
    y = models.FloatField()
    image = models.ImageField(null=True,default=None) 
    opening_hours = models.TextField(default='')

    def __str__(self):
        return self.Restaurant_name

class Booking(models.Model):
    username = models.CharField(max_length=100)
    number_of_seats = models.IntegerField()
    message = models.TextField(default=None)
    Restaurant_booking = models.ForeignKey(Restaurant,on_delete=models.CASCADE,default=None,null=True)

    def __str__(self):
        return f'{self.Restaurant_booking},{self.number_of_seats},{self.username}'
        



    











    
