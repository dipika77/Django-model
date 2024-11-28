# from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from authentication import views
# from . import views yo vitra kai denote dot le


urlpatterns = [
     path('login/', views.login),
     path('register/',views.register),
]




