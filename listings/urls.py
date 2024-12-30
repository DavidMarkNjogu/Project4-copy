# listings/urls.py

from django.urls import path
from .views import listings_list, listing_detail

app_name = 'listings'

urlpatterns = [
    path('',listings_list, name='listings_list'),
    path('<int:listing_id>/',listing_detail, name='listing_detail'),

]
