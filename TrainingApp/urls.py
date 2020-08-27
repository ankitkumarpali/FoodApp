from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
	# path('',views.home, name = 'home'),
	path('',views.restaurant, name = "restaurant"),
	path('order/', views.order_detail, name = 'order'),
	path('restaurant/<str:pk>', views.Restaurant_detail.as_view(), name = 'restaurant_detail'),
]