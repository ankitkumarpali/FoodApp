from django.urls import resolve, reverse
from django.test import SimpleTestCase
from TrainingApp.views import restaurant, Restaurant_detail, order

class TestUrls(SimpleTestCase):

	def test_restaurant_is_resolved(self):
		url = reverse('restaurant')
		self.assertEquals(resolve(url).func, project_list)

	def test_restaurant_resolved(self):
		url = reverse('restaurant_detail')
		self.assertEquals(resolve(url).func.view_class,Restaurant_detail)

	def test_order_resolved(self):
		url = reverse('order')
		self.assertEquals(resolve(url).func, order)