from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import *
from .api import *
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib import auth
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from rest_framework.authtoken.models import Token
from django.conf import settings
from .aws_lambda import *

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
        return decoded_data
    except jwt.ExpiredSignatureError:
        return Response({'error': 'Expired token'}, status=401)
    except jwt.InvalidTokenError:
        return JsonResponse({'error': 'Invalid token'}, status=403)

#response status: 200 OK, 401 NOT AUTHORIZED, 403 FORBIDDEN (token expired)

class CheckAuthenticatedView(APIView):
    def get(self, request, format=None):
        user = self.request.user

        try:
            isAuthenticated = user.is_authenticated

            if isAuthenticated:
                return Response({ 'isAuthenticated': 'success' })
            else:
                return Response({ 'isAuthenticated': 'error' })
        except:
            return Response({ 'error': 'Something went wrong when checking authentication status' })


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

class TestView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        id = data['id']

        try:
            print("exist")
            p= Prescription.objects.get(id=id)
            return Response({p})
        except Prescription.DoesNotExist:
            print("doesnt exist")
            return Response({'prescription': "error_id"})


def testing_lambda(request):
    #put here the name of the function u want to test
    findUserByUsername()
    hello()
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

