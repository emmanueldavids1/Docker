from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.

def home_view(request):
    return HttpResponse('This is the home page.')

def about_view(request):
    return HttpResponse('This is the about page.')