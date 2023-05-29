from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import *
import jwt
import datetime
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib import auth
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from rest_framework.authtoken.models import Token
from django.conf import settings
from .aws_lambda import *
from .aws_step import *
import re

def generate_token(id,password):
    return jwt.encode({
        'user_id': id,
        'user_password': password,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

def decode_token(token):
    try:
        decoded_data = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        # if i actually want to check in the db the id and password, i dont think its necessary, but if it were to be done it would be here
        print("decoded token")
        print(decoded_data)
        return None
    except jwt.ExpiredSignatureError:
        return Response({'error': 'Expired token'}, status=401)
    except jwt.InvalidTokenError:
        return Response({'error': 'Invalid token'}, status=403)

#response status: 200 OK, 401 NOT AUTHORIZED, 403 FORBIDDEN (token expired), 404 NOTFOUND
def authorization(meta):

    header_item = next((item for item in meta.items() if item[0] == 'HTTP_COOKIE'), None)

    if header_item!=None:
        return decode_token(header_item[1].split("BearerToken=")[1])
    else:
        print("no auth")
        return Response({'error': 'No token provided'}, status=404)



class LoginView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        username = data['username']
        password = data['password']

        try:
            print("exist")
            User.objects.get(username=username, password=password, pharmacist=True)
            token = generate_token(username, password)

            return Response({'token': token})
        except User.DoesNotExist:
            print("doesnt exist")
            return Response({'token': "login_error"})

class OrderView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        print("inside order view")

        auth_error= authorization(request.META)
        if auth_error !=None:
            return auth_error
        print("after auth")

        
        data = self.request.data

        id = data['id']
        try:
            print("exist: id "+ id)

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
            
            authorization_header = self.request.META.get('HTTP_AUTHORIZATION')
            print("Authorization header:", authorization_header)
            return Response({'prescription': prescriptions_data})
        except Prescription.DoesNotExist:
            print("doesnt exist")
            return Response({'prescription': "prescription_error"})

class StartOrderView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        auth_error= authorization(request.META)
        if auth_error !=None:
            return auth_error
        print("after auth")
        data = self.request.data

        order = data['order']
        print("exist: order ")
        print(order)

        for med in order["medications"]: #{'medication_id': 1, 'name': 'brufen', 'price': 10, 'alternatives': []}
            del med["alternatives"]

        print(order)


        status, order_status =lambda_start_order(order)

        print("status: ")
        print(status)
        print(order_status)

        if status:
            return Response({'update': "db updated",'order_status': order_status})   
        else:
            return Response({'error': "db error", 'order_status': order_status})
            

class UpdateOrderView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        auth_error= authorization(request.META)
        if auth_error !=None:
            return auth_error
        print("after auth")
        data = self.request.data

        order_id = data['id']
        update_function = data['update_function']

        #get the lambda functions

        order_status=lambda_update_order(order_id, update_function)

        if order_status== None:
            return Response({'error': "db error"})
        else:
            return Response({'update': "db updated",'order_status': order_status})

class RekognitionView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        auth_error= authorization(request.META)
        if auth_error !=None:
            return auth_error
        print("after auth")

        img = self.request.FILES.get('image')

        if img is None:
            return Response({'error': 'no image found'})

        img_binary = img.read()        
        name= rekognition(img_binary)

        if name== None:
            return Response({'error': "no match found"})
        else:

            #get the lambda function that updates the status so the order is confirmed as payed
            status=step_start_exe(request)
            #temp_status=lambda_update_order(order_id, update_function)
            return Response({'rekognition': name, 'order_status': status})

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