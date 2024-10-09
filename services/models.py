from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from users.models import *
from django.utils import timezone



class BookingRequest(models.Model):
    client_name = models.ForeignKey(User, on_delete=models.CASCADE) 
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='provider_bookings')
    booking_date = models.DateTimeField(default=timezone.now)
    start_time = models.TimeField()
    end_time = models.TimeField()
    about_work = models.TextField(null=True, blank=True)   
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
         ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('Completed', 'Completed'),
    ], default='Pending')
    is_completed = models.BooleanField(default=False)  
    is_confirmed = models.BooleanField(default=False)  
    payment_status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Transferred', 'Transferred'),
    ], default='Pending')
    def __str__(self):
        return f"Booking by {self.client_name.username} with {self.provider}"

class Message(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    booking = models.ForeignKey(BookingRequest, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE,default=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('accepted', 'Accepted'), ('rejected', 'Rejected')])
    payment_url = models.URLField(null=True, blank=True)
    def __str__(self):
        return f"Message to {self.client.username} - {self.status}"