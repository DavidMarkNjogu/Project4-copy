from django.shortcuts import render, redirect, get_object_or_404  # Importing render and redirect functions
from django.contrib import messages  # Importing messages for notifications
from .models import Booking  # Importing the Booking model
from listings.models import PropertyListing  # Importing the PropertyListing model
from django.core.exceptions import ValidationError  # Importing ValidationError for handling validation errors

def book_listing(request):
    if request.method == 'POST':
        property_id = request.POST.get('property_id') # Get the selected property ID
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        # Create a new booking instance
        booking = Booking(
            user=request.user,  # Assuming the user is logged in
            property_listing_id=property_id,
            start_date=start_date,
            end_date=end_date,
        )
        
        try:
            booking.clean()  # Validate the booking dates
            booking.save()  # Save the booking to the database
            messages.success(request, f"Booking for property ID {property_id} from {start_date} to {end_date} was added successfully!")
            print(f"Redirecting to booking success for booking ID: {booking.id}")  # Debugging statement
            return redirect('booking_success', booking_id=booking.id)  # Redirect to the success page with booking ID
        except ValidationError as e:
            messages.error(request, str(e))  # Capture validation errors
            return render(request, 'bookings/book_form.html', {'error_message': str(e)})

    # Fetch available listings to display in the dropdown
    listings = PropertyListing.objects.filter(status='Available')  # Adjust the filter as needed      
    return render(request, 'bookings/book_form.html', {'listings': listings})  # Pass listings to the template

def booking_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)  # Fetch the booking using the booking ID
    return render(request, 'bookings/booking_success.html', {'booking': booking})  # Render the success template with booking details
    #return render(request, 'bookings/book_form.html')  # Render the booking form