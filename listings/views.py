from django.shortcuts import render, get_object_or_404, redirect
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
        form = PropertyListingForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('listings:listings_list')
    else: 
        form = PropertyListingForm()
    return render(request, 'listings/listing_create.html', {'form': form})

def listing_update(request, listing_id):
    listing = get_object_or_404(PropertyListing, id=listing_id)
    form = PropertyListingForm(instance=listing)

    if request.method == 'POST':
        form = PropertyListingForm(request.POST, files=request.FILES,  instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listings:listing_detail', listing_id=listing_id)
    
    else:
        return render(request, 'listings/listing_update.html', {'form': form})

def listing_delete(request, listing_id):
    listing = get_object_or_404(PropertyListing, id=listing_id)
    if request.method == 'POST':
        listing.delete()
        return redirect('listings:listings_list')
    