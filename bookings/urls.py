from django.urls import path
from . import views

urlpatterns = [
    path('venues/', views.VenueListView.as_view(), name='venue-list'),
    path('venues/<int:pk>/', views.VenueDetailView.as_view(), name='venue-detail'),
    path('bookings/', views.BookingListView.as_view(), name='booking-list'),
    path('bookings/create/', views.BookingCreateView.as_view(), name='booking-create'),
    path('', views.home, name='home'),  # homepage
]

