from django.contrib import admin
from django.urls import path, re_path
from . import views


urlpatterns = [
    #pages
    path("", views.index, name="index"),
    path("testing/", views.testing_lambda, name="lambda"),
    path("login/",views.login, name="login"),
    path("scanner/", views.scanner, name="scanner"),
    path(f"prescription/<int:id>/",views.prescription, name="prescription"),

    #API
    path('api/prescription/<int:id>/', views.prescription_api, name='prescription_api'),
    path('api/prescriptions/', views.prescriptions_api, name='prescriptions_api'),
    #path('api/login/', views.login_api, name='login_api'),

    path('authview/', views.CheckAuthenticatedView.as_view()),
    path('api/login', views.LoginView.as_view()),

    #default
    re_path(r'^.*$', views.not_found, name="not_found"),

]