from django.urls import path

from . import views

urlpatterns = [
    path("try/", views.trying , name="trying"),
    path("index/", views.index, name="index"),
    path("login/",views.login, name="login"),
]