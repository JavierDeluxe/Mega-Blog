from django.contrib import admin
from django.urls import path
from .views import *

app_name = "articles"

urlpatterns = [
    path("", index,name="index"),
    path("register", Register.as_view(),name="register"),
    path("sing_in", Login.as_view(), name="login"),
    path("logout",LogOut.as_view(), name="logout"),
    path("registrar", RegisterArticle.as_view(),name="register-article"),
    path("ver_articulo/<int:id>",watch_articulo, name="watch_article")
]


