from django.contrib import admin
from .models import Restaurants, Dishes, Order
# Register your models here.
admin.site.register(Restaurants)
admin.site.register(Dishes)
admin.site.register(Order)