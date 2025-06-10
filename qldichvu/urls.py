from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('service-1/', views.service_1, name='service 1'),
    path('service-2/', views.service_2, name='service 2'),
    path('service-3/', views.service_3, name='service 3'),
    path('services/', views.services, name='services'),
]