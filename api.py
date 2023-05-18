from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Prescription
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from .aws_lambda import *
import jwt
import datetime
import json

def order_api(request):
    #TODO
    p= Prescription.objects.get(pk=1)

    medication_data = []
    for medication in p.medications.all():
        medication_dict = {
            'medication_id': medication.pk,
            'name': medication.name,
            'price': medication.price,
            'alternatives': []
        }
        for alternative in medication.alternatives.all():
            medication_dict['alternatives'].append({
                'medication_id': alternative.pk,
                'name': alternative.name,
                'price': alternative.price
            })
        medication_data.append(medication_dict)

    prescriptions_data = []
    prescriptions_data.append({
            'prescription_id': p.pk,
            'expiration': p.expiration_date,
            'patient': p.patient.name,
            'status': p.status,
            'filled': p.filled,
            'medications': medication_data,
            # Add other prescription data here
        })
    return JsonResponse(prescriptions_data, safe=False)


def startfunction_api(request):
    #TODO get json prescription through the request body

    p= {"prescription_id": 1, "expiration": "2023-06-17T05:14:49Z", "patient": "random", "status": 0, "filled": false, "medications": [{"medication_id": 1, "name": "brufen", "alternatives": []}, {"medication_id": 3, "name": "benuron", "alternatives": [{"medication_id": 2, "name": "paracetamol"}]}]}
    lambda_get_prescription(p)

    return JsonResponse({"message": "success"}, safe=False)




def prescription_api(request, id):
    return JsonResponse("prescriptions_data", safe=False)


def prescriptions_api(request):
    prescriptions = Prescription.objects.all()
    prescriptions_data = []
    for prescription in prescriptions:
        prescriptions_data.append({
            'prescription_id': prescription.pk,
            'expiration': prescription.expiration_date,
            'patient': prescription.patient.name,
            'status': prescription.status,
            'filled': prescription.filled,
            # Add other prescription data here
        })
    return JsonResponse(prescriptions_data, safe=False)