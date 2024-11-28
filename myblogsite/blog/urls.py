# from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from blog import views

urlpatterns = [
     path('', views.home),
     path('post/',views.post),
     path('post_detail/',views.post_detail),
]




