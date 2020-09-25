from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	return render(request, 'firstapp/home.html')

# def about(request):
# 	return HttpResponse("About page")

# def contact(request):
# 	return HttpResponse("Contact us")