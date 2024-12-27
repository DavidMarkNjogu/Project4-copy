from django.contrib import admin  # Importing the admin module
from .models import Booking  # Importing the Booking model

# Registering the Booking model to make it accessible in the admin interface
admin.site.register(Booking)