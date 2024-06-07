from django.contrib import admin
from .models import Customer, Order, Item

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Item)
