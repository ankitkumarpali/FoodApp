from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Restaurants(models.Model):
	rest_name = models.CharField(max_length = 30)
	rest_add = models.CharField(max_length = 30)
	def __str__(self):
		return self.rest_name

class Dishes(models.Model):
	restuarant = models.ForeignKey(Restaurants,on_delete = models.CASCADE)
	dish_name = models.CharField(max_length = 30)
	dish_price = models.IntegerField(default = 0)
	def __str__(self):
		return self.dish_name

class Order(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	dishes = models.ForeignKey(Dishes, on_delete = models.CASCADE)
	restuarant = models.ForeignKey(Restaurants, on_delete = models.CASCADE)
	tot_quantity = models.IntegerField(default = 0)
	
