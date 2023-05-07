from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Prescription
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
import jwt
import datetime
import json

def login_api(request):
    print("login_api")
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Generate JWT token
            token = jwt.encode({
                'user_id': user.pk,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expiration time
            }, 'your_secret_key', algorithm='HS256')

            return JsonResponse({'token': token.decode()})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)





def prescription_api(request, id):
    prescription = get_object_or_404(Prescription, pk=id)
    medication_data = []
    for medication in prescription.medications.all():
        medication_dict = {
            'medication_id': medication.pk,
            'name': medication.name,
            'alternatives': []
        }
        for alternative in medication.alternatives.all():
            medication_dict['alternatives'].append({
                'medication_id': alternative.pk,
                'name': alternative.name
            })
        medication_data.append(medication_dict)

    prescription_data = {
        'prescription_id': prescription.pk,
        'expiration': prescription.expiration_date,
        'patient': prescription.patient.name,
        'patient_id': prescription.patient.pk,
        'status': prescription.status,
        'filled': prescription.filled,
        'medications': medication_data
        # Add other prescription data here
    }
    return JsonResponse(prescription_data)

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