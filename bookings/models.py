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
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)
    attendees = models.IntegerField()

    def __str__(self):
        return f"{self.customer_name} - {self.venue.name} on {self.date}"
