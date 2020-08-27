# Create your views here.
from django.shortcuts import render
import logging
from .models import Restaurants, Dishes, Order
import json
from django.views.generic import View
# Create your views here.
from django.shortcuts import render, HttpResponse, \
    HttpResponseRedirect
from django.http import JsonResponse

logger = logging.getLogger(__name__)

def home(request):
	return HttpResponse('<h1>home</h1>')

def restaurant(request):
	restaurant_obj = Restaurants.objects.all()
	my_text = {
		'restaurant':restaurant_obj
	}
	return render(request,'TrainingApp/restaurant.html',my_text)

class Restaurant_detail(View):
	def get(self, request, pk, *args, **kwargs):
		dish_result = Dishes.objects.filter(restuarant_id = pk).values('dish_name','dish_price','id')

		all_dishes = []
		# for dish in dish_result:
		# 	print(dish)
		# 	ele = {
		# 		'dish_name': dish['dish_name'],
		# 		'dish_price': dish['dish_price,
		# 		'dish_id': dish.id,
		# 	}
		# 	all_dishes.append(ele)
		json_data = json.dumps(list(dish_result))
		return HttpResponse(json_data, 'application/json')

def order_detail(request):
	data = json.loads(request.body)
	rest_id = data['restaurants']
	user_id = request.user.id

	for dish in data['dish']:
		order = Order(user_id = user_id, restuarant_id = rest_id, dishes_id = dish['dish_id'], quantity = dish['quantity'])
		order.save()
	response = {
        'status': 200,
        'message': 'Your order has been placed successfully!'
	}

	return JsonResponse(response, safe = True)