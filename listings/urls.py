# listings/urls.py

from django.urls import path
from .views import listings_list, listing_detail

urlpatterns = [
    path('',listings_list, name='listings'),
    path('<int:listing_id>/',listing_detail, name='listing_detail'),

]
