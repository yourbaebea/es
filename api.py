from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Prescription

#print(prescription.__dict__)
#for any api calls, if u dont know how it is organized do this print

    
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