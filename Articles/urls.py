from django.contrib import admin
from django.urls import path
from .views import *

app_name = "articles"

urlpatterns = [
    path("", index,name="index"),
    path("register", Register.as_view(),name="register"),
    path("sing_in", Login.as_view(), name="login")
]


