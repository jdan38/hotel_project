from django.shortcuts import get_object_or_404, render 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .choice import  bedroom_choices, bedsize_choices, price_choices, state_choices
from .models import Listing
from .models import Hotel


def index(request):

    #listings = Listing.objects.order_by('price').filter(is_occupied=True)
    listings = Listing.objects.all()
    hotels = Hotel.objects.all()

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)
    
    

    context = {
        'listings': paged_listing,
        'hotels': hotels
       
    }
    return render(request, 'listings/listings.html',context)


def listing(request, id):
    listing = get_object_or_404(Listing, pk=id)

    contextl = {
        'listing' : listing
    }
    return render(request, 'listings/listing.html', contextl)


def search(request):
	queryset_list = Listing.objects.order_by('-roomnumber')
	hotels = Hotel.objects.all()
    
	# Keywords
	if 'keywords' in request.GET:
		keywords = request.GET['keywords']
		if keywords:
			queryset_list = queryset_list.filter(title__icontains=keywords)
    
    # City
	if 'city' in request.GET:
		city = request.GET['city']
		if city:
			hotels = hotels.filter(city__iexact=city)
    
    # State
	if 'state' in request.GET:
		state = request.GET['state']
		if state:
			hotels = hotels.filter(state__iexact=state)
		
	# Price
	if 'price' in request.GET:
		price = request.GET['price']
		if price:
			queryset_list = queryset_list.filter(price__lte=price)

    # Room Type
	# if 'title' in request.GET:
	# 	title = request.GET['title']
	# 	if title:
	# 		queryset_list = queryset_list.filter(title__iexact=title)

	contexts = {
        
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'bedsize_choices': bedsize_choices,
        'listings': queryset_list,
        'hotels': hotels
    }
	return render(request, 'listings/search.html', contexts)
     


