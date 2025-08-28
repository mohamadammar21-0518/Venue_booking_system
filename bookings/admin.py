from django.contrib import admin
from .models import Venue, Booking


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'capacity')
    search_fields = ('name', 'location')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'venue', 'date', 'time_slot', 'attendees', 'status')
    list_filter = ('status', 'venue', 'date', 'time_slot')
    search_fields = ('customer_name', 'customer_email')
    ordering = ('-date',)

    # ✅ Allow inline editing of booking status + time_slot
    list_editable = ('status', 'time_slot')
