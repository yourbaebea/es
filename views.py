from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Prescription
from .api import prescription_api

def not_found(request):
    return render(request, 'index.html')


def index(request):
    return render(request, 'index.html')

def scanner(request):
    token = "your_token_value"
    # Render the index template and set the token value in the response headers
    response = render(request, 'index.html', {'token': token})
    response['prescription_id'] = id
    return response

def prescription(request,id):
    try:
        prescription = Prescription.objects.get(pk=id)
        return render(request, 'index.html', {'prescription': prescription})
    except Prescription.DoesNotExist:
        print('Prescription with id {} does not exist'.format(id))
        return HttpResponse('An error occurred while fetching the prescription.')


def login(request):
    
    token = "your_token_value"

    # Render the index template and set the token value in the response headers
    response = render(request, 'index.html', {'token': token})
    response['X-Token'] = token

    return response