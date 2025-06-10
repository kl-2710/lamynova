from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('pages/', views.pages, name='pages'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_details, name='blog_details'),
    path('faq/', views.faq, name='faq'),
 

]