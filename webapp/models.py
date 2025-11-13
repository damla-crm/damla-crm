from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customers')
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    country = models.CharField(max_length=100, blank=True)
    visaType = models.CharField(max_length=50, blank=True)
    personCount = models.PositiveIntegerField(null=True, blank=True)
    services = models.JSONField(null=True, blank=True)

    totalAmount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    paymentStatus = models.CharField(max_length=30, blank=True)
    saleNotes = models.TextField(blank=True)
    saleDate = models.DateTimeField(null=True, blank=True)

    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.phone})"
