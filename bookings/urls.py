from django.urls import path  # Importing path for URL routing
from .views import book_listing, booking_success  # Importing the booking view

urlpatterns = [
    path('book/', book_listing, name='book_form'),  # URL for the booking form
    path('booking-success/<int:booking_id>/', booking_success, name='booking_success'),  # Success page URL
    
]