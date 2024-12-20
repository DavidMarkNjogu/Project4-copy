from django.db import models

class PropertyListing(models.Model):
    PROPERTY_TYPES = [
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('condo', 'Condo'),
        ('townhouse', 'Townhouse'),
        ('villa', 'Villa'),
        ('studio', 'Studio'),
        ('duplex', 'Duplex'),
        ('commercial', 'Commercial'),
        ('other', 'Other'),
    ]

    SALE_STATUS_CHOICES = [
        ('sale', 'For Sale'),
        ('rent', 'For Rent'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPES)
    num_bedrooms = models.IntegerField(default=1)
    num_bathrooms = models.IntegerField(default=1)
    image = models.ImageField(upload_to='realestate_images/', blank=True, null=True)
    status = models.CharField(max_length=20, default='Available')
    sale_status = models.CharField(max_length=10, choices=SALE_STATUS_CHOICES, default='sale')

    def __str__(self):
        return self.title
