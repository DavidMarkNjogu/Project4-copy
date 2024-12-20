# listings/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.listings, name='listings'),
    path('<int:listing_id>/', views.listing_detail, name='listing_detail'),
]
