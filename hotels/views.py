from django.shortcuts import render
from .models import Hotel


def index(request):
    hotels = Hotel.objects.all()
    

    contexth = {
        'hotels': hotels
    }
    return render(request, 'hotels/hotels.html',contexth)

def hotels(request):
    return render(request, 'hotels/hotel.html')
