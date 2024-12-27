from django.urls import path  # Importing path for URL routing
from .views import book_property  # Importing the booking view

urlpatterns = [
    path('book/', book_property, name='book_form'),  # URL for the booking form
]