from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def another_test(request):
    return HttpResponse("Hello, world. This is another test!")
