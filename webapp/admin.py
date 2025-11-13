from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "email", "visaType", "totalAmount", "paymentStatus", "user")
    list_filter = ("visaType", "paymentStatus", "user")
    search_fields = ("name", "phone", "email")

# Register your models here.
