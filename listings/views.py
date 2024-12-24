# listings/views.py

from django.shortcuts import render, get_object_or_404
from .models import PropertyListing

def listings_list(request):
    listings = PropertyListing.objects.all()
    return render(request, 'listings/listings.html', {'listings': listings})

def listing_detail(request, listing_id):
    listing = get_object_or_404(PropertyListing, pk=listing_id)
    return render(request, 'listings/listing_detail.html', {'listing': listing})

