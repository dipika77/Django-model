# from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return HttpResponse("welcome to login page")
def register(request):
    return HttpResponse("registration successful.")

# Create your views here.
