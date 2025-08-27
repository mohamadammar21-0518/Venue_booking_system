from django.shortcuts import render
from django.views import generic
from .models import Venue, Booking

# Homepage
def home(request):
    return render(request, 'bookings/home.html')

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
    context_object_name = 'bookings'  # <- important
 # so we can loop over 'bookings' in template

class BookingCreateView(generic.CreateView):
    model = Booking
    fields = ['customer_name', 'customer_email', 'attendees', 'venue', 'date']
    template_name = 'bookings/booking_form.html'
    success_url = '/bookings/'

    # Optional: populate default date if empty
    def form_valid(self, form):
        if not form.cleaned_data.get('date'):
            import datetime
            form.instance.date = datetime.date.today()
        return super().form_valid(form)
