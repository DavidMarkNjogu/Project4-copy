from django.shortcuts import render, get_object_or_404
from .models import PropertyListing
from .forms import PropertyListingForm

def listings_list(request):
    listings = PropertyListing.objects.all()
    return render(request, 'listings/listings.html', {'listings': listings})

def listing_detail(request, listing_id):
    listing = get_object_or_404(PropertyListing, pk=listing_id)
    return render(request, 'listings/listing_detail.html', {'listing': listing})

def listing_create(request):
    if request.method == 'POST':
        form = PropertyListingForm()
        if form.is_valid():
            form.save()
            return redirect('listings:listings_list')
    else:
        form = PropertyListingForm()
    return render(request, 'listings/listing_create.html', {'form': form})
