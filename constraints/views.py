from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Greetings! This is the default response!")

