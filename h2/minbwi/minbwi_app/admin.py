from django.contrib import admin

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'number_of_seats', 'message', 'Restaurant_booking', 'Status', 'Confirm')
    list_filter = ['Status']
    list_filter = ['Restaurant_booking']

# Register your models here.
from .models import Booking, Restaurant,Region
admin.site.register(Restaurant)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Region)