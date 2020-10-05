from django.urls import path
from firstapp import views			#-> importing functions from views.py

urlpatterns = [
    path('home/', views.home),
    path('register/', views.create, name='register'),
    path('success/', views.success, name='success'),
    # path('register/', views.form_view, name='register')
    # path('about', views.about),
    # path('contact-us', views.contact),
]