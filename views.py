from django.http import HttpResponse

def login(request):
    return HttpResponse("Hello, world. You're at the login.")

def index(request):
    return HttpResponse("Hello, world. You're at the index.")


