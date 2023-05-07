from django.urls import path, re_path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login/",views.login, name="login"),
    path("scanner/", views.scanner, name="scanner"),
    path(f"prescription/<int:id>/",views.prescription, name="prescription"),

    #API
    path('api/prescription/<int:id>/', views.prescription_api, name='prescription_api'),
    path('api/prescriptions/', views.prescriptions_api, name='prescriptions_api'),




    re_path(r'^.*$', views.not_found, name="not_found"),

]