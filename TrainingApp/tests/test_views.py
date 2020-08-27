from django.test import TestCase, Client
from TrainingApp.models import Dishes, Restaurants, Order
import json
from django.urls import resolve, reverse
class TestViews(TestCase):

	def test_restaurant(self):
		client = Client()

		response = client.get(reverse('restaurant'))
		self.asserEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'TrainingApp/restaurant.html')
	def test_restaurant_list(self):
		client = Client()

		response = client.get(reverse('restaurant_detail'))
		self.asserEquals(response.status_code, 200)
		


