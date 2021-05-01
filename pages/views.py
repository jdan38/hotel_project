from django.shortcuts import render
from django.http import HttpResponse
from listings.choice import  bedroom_choices, bedsize_choices, price_choices, state_choices

from listings.models import Listing
from staff.models import Staff

def index(request):
   
    listings = Listing.objects.all()
    
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'bedsize_choices': bedsize_choices,
    }
  
    return render(request, 'pages/index.html', context )

def about(request):
    # Get all realtors
    #realtors = Realtor.objects.order_by('-hire_date')

    #Get MVP
    #mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    contexta = {
            #'realtors': realtors,
           # 'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', contexta)

def contact(request):
    return render(request, 'pages/contact.html')

