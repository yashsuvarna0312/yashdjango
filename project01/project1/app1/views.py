from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def Home(request):
    return HttpResponse("Hello, this is my view!")