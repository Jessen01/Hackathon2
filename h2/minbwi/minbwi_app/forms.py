from django import forms

class Booking(forms.Form):
    username = forms.CharField(max_length=100)
    number_of_seats = forms.IntegerField()
    message = forms.CharField(max_length=100)


