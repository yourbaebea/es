from django.http import HttpResponse

def login(request):
    return HttpResponse("Hello, world. You're at the login endpoint.")

def index(request):
    return HttpResponse("Hello, world. You're at the index endpoint.")


def trying(request):
    return HttpResponse("Hello, world. You're at the trying endpoint.")


