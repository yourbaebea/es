from django.contrib import admin
from django.urls import path, re_path
from . import views


urlpatterns = [
    #pages
    path("", views.index, name="index"),
    path("order/", views.index, name="order"),
    path("testing/", views.testing_lambda, name="lambda"),
    path("login/",views.login, name="login"),
    path("scanner/", views.index, name="scanner"),

    #API
    path('api/prescriptions/', views.prescriptions_api, name='prescriptions_api'),
    path('api/order/', views.order_api, name='order_api'),
    #path('api/test/', views.TestView.as_view()),
    path('api/login', views.LoginView.as_view()),
    path('api/startfunction/', views.startfunction_api),

    #default
    re_path(r'^.*$', views.index, name="not_found"),

]