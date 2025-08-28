from django.shortcuts import render
from django.views import generic
from .models import Venue, Booking


# Homepage (Dashboard)
def home(request):
    total_venues = Venue.objects.count()
    total_bookings = Booking.objects.count()
    pending_bookings = Booking.objects.filter(status='pending').count()

    context = {
        'total_venues': total_venues,
        'total_bookings': total_bookings,
        'pending_bookings': pending_bookings,
    }
    return render(request, 'bookings/home.html', context)


# Class-based views for venues
class VenueListView(generic.ListView):
    model = Venue
    template_name = 'bookings/venue_list.html'


class VenueDetailView(generic.DetailView):
    model = Venue
    template_name = 'bookings/venue_detail.html'


# Class-based views for bookings
class BookingListView(generic.ListView):
    model = Booking
    template_name = 'bookings/booking_list.html'
    context_object_name = 'bookings'  # so we can loop over 'bookings' in template


class BookingCreateView(generic.CreateView):
    model = Booking
    fields = [
        'customer_name',
        'customer_email',
        'attendees',
        'venue',
        'date',
        'time_slot',   # ✅ added so users can pick slot
    ]
    template_name = 'bookings/booking_form.html'
    success_url = '/bookings/'

    # Optional: populate default date if empty
    def form_valid(self, form):
        if not form.cleaned_data.get('date'):
            import datetime
            form.instance.date = datetime.date.today()
        # status will default to "pending", no need to expose in form
        return super().form_valid(form)
