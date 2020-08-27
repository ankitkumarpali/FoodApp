from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from .forms import RegisterForm
# Create your views here.

def register(response):
	# return HttpResponse('<h1>hello</h1>')
	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()
	else:
		form = RegisterForm()

	return render(response, "register/register.html",{'form':form})

