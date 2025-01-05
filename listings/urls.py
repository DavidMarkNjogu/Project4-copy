# listings/urls.py

from django.urls import path
from .views import listings_list, listing_detail, listing_create, listing_update, listing_delete

app_name = 'listings'

urlpatterns = [
    path('',listings_list, name='listings_list'),
    path('<int:listing_id>/',listing_detail, name='listing_detail'),
    path('create/',listing_create, name='listing_create'),
    path('update/<int:listing_id>/',listing_update, name='listing_update'),
    path('delete/<int:listing_id>/',listing_delete, name='listing_delete'),

]
