from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    return HttpResponse("Hello, world. You're at the login endpoint.")

def index(request):
    return render(request, 'index.html' )
