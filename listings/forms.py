from django.forms import ModelForm
from .models import PropertyListing

class PropertyListingForm(ModelForm):
    class Meta:
        model = PropertyListing
        fields = 'title', 'description', 'price', 'location', 'property_type', 'num_bedrooms', 'num_bathrooms', 'image', 'status', 'sale_status'



