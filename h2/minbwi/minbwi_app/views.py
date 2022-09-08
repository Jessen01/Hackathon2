from django.http import HttpResponse
from django.shortcuts import render
from .models import Booking, Restaurant

# Create your views here.

def index(request):
    return render(request,'index.html')

def addbooking(request):
    if(request.method == "POST"): 
        request.POST.get('name')
        request.POST.get('region')
        request.POST.get('seat')
        request.POST.get('message')
        print( request.POST.get('name'))
        print(request.POST.get('region'))
        resto =Restaurant.objects.filter(Restaurant_name='Le Pain Maison')[0]
        x = Booking(Restaurant_booking =resto,number_of_seats=request.POST.get('seat'),message=request.POST.get('message'))
        x.save()

        return HttpResponse("Your booking has been saved")
    return HttpResponse("Please use post")



