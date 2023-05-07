from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Prescription
from .api import prescription_api, prescriptions_api, login_api
from django.contrib.auth import get_user_model, login, logout

from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib import auth
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from rest_framework.authtoken.models import Token


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

        #TODO auth is not working not sure how to do it

        """
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)
        """
        token= "123token"


        return Response({'token': token, 'user': username, 'password': password})
        




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

