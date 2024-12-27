from django.shortcuts import render, redirect  # Importing render and redirect functions
from django.contrib import messages  # Importing messages for notifications
from .models import Booking  # Importing the Booking model
from django.core.exceptions import ValidationError  # Importing ValidationError for handling validation errors

def book_property(request):
    if request.method == 'POST':
        property_id = request.POST.get('property_id')
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
            return redirect('book_form')  # Redirect to the booking form page
        except ValidationError as e:
            messages.error(request, str(e))  # Capture validation errors
            return render(request, 'bookings/book_form.html', {'error_message': str(e)})

    return render(request, 'bookings/book_form.html')  # Render the booking form