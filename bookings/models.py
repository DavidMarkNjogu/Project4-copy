from django.db import models  # Importing the models module from Django
from django.conf import settings  # Importing settings to use the user model
from listings.models import PropertyListing  # Importing the PropertyListing model for foreign key relationship
from django.core.exceptions import ValidationError  # Importing ValidationError for custom validation

class Booking(models.Model):
    # Foreign key to the user model, allowing multiple bookings per user
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    
    # Foreign key to the PropertyListing model, allowing multiple bookings for the same property
    property_listing = models.ForeignKey(PropertyListing, on_delete=models.CASCADE)  
    
    # Automatically set the booking date when a booking is created
    booking_date = models.DateTimeField(auto_now_add=True)  
    
    # Start and end dates for the booking
    start_date = models.DateField()  
    end_date = models.DateField()  
    
    # Choices for the booking status
    STATUS_CHOICES = [
        ('pending', 'Pending'),  # Booking is pending
        ('confirmed', 'Confirmed'),  # Booking is confirmed
        ('cancelled', 'Cancelled'),  # Booking is cancelled
    ]
    # Status of the booking, default is 'pending'
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')  

    # Custom validation to ensure end date is after start date
    def clean(self):
        if self.start_date >= self.end_date:
            raise ValidationError('The end date must be after the start date.')

    # String representation of the booking instance
    def __str__(self):
        return f"Booking by {self.user.username} for {self.property_listing.title} from {self.start_date} to {self.end_date}"