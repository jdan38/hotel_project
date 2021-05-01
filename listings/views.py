from django.shortcuts import get_object_or_404, render 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .choice import  bedroom_choices, bedsize_choices, price_choices, state_choices
from .models import Listing


def index(request):

    #listings = Listing.objects.order_by('price').filter(is_occupied=True)
    listings = Listing.objects.all()

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)
    
    

    context = {
        'listings': paged_listing
       
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
	
	# Keywords
	if 'keywords' in request.GET:
		keywords = request.GET['keywords']
		if keywords:
			queryset_list = queryset_list.filter(description__icontains=keywords)

		
	
	context = {
        
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'bedsize_choices': bedsize_choices,
        'listings': queryset_list
    }
	return render(request, 'listings/search.html', context)
     

