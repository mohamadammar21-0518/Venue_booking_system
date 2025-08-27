
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Each venue that can be booked
class Venue(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


# Booking by a user for a specific venue
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # who booked
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE) # which venue
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.user.username} - {self.venue.name} ({self.status})"

