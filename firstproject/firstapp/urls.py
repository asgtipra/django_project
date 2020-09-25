from django.urls import path
from firstapp import views			#-> importing home function from views.py

urlpatterns = [
    path('home', views.home),
    # path('about', views.about),
    # path('contact-us', views.contact),
]