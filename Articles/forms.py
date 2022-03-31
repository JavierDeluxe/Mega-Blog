from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class RegistroForm(UserCreationForm):
  
    class Meta():
        model = UserProfile
        fields = ("username", "email", "password1","password2","photo")
        labels = {"username":"Nombre completo", "email": "Correo","password1":"Ingrese contraseña","password2":"Confirme contraseña","photo":"Cargue una imagen"}

