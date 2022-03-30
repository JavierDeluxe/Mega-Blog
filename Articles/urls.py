from django.contrib import admin
from django.urls import path
from . import views
from .views import Register

app_name = "articles"

urlpatterns = [
    path("",views.index,name="index"),
    path("register.html/",Register.as_view(),name="register"),
]


