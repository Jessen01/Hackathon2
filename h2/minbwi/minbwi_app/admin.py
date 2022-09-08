from django.contrib import admin

# Register your models here.
from .models import Booking, Restaurant,Region
admin.site.register(Restaurant)
admin.site.register(Booking)
admin.site.register(Region)