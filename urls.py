from django.contrib import admin
from django.urls import path, re_path
from . import views


urlpatterns = [
    #pages
    path("", views.index, name="index"),
    path("order/", views.index, name="order"),
    path("login/",views.login, name="login"),
    path("scanner/", views.index, name="scanner"),

    #API
    path('api/login', views.LoginView.as_view()),
    path('api/order', views.OrderView.as_view()),
    path('api/startorder', views.StartOrderView.as_view()),
    path('api/updateorder', views.UpdateOrderView.as_view()),
    path('api/rekognition', views.RekognitionView.as_view()),

    #default
    re_path(r'^.*$', views.index, name="not_found"),

]