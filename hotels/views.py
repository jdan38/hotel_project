from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Hotel


def index(request):
    hotels = Hotel.objects.all()

    paginator = Paginator(hotels, 6)
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)
    

    contexth = {
        'hotels': paged_listing
    }
    return render(request, 'hotels/hotels.html',contexth)

def hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)

    context = {
        'hotel': hotel
    }
    return render(request, 'hotels/hotel.html', context)

