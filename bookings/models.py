from django.db import models

# Venue model
class Venue(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# Booking model
class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    TIME_SLOT_CHOICES = [
        ('FULL', 'Whole Day'),
        ('EVE1', '8:30 PM - 10:00 PM'),
        ('EVE2', '10:00 PM - 11:30 PM'),
    ]

    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    date = models.DateField()
    time_slot = models.CharField(
        max_length=10,
        choices=TIME_SLOT_CHOICES,
        default='FULL'
    )
    attendees = models.IntegerField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    def __str__(self):
        return f"{self.customer_name} - {self.venue.name} on {self.date} [{self.get_time_slot_display()}] [{self.status}]"
