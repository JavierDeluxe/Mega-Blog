from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import UserProfile


class RegistroForm(UserCreationForm):
  
    class Meta():
        model = UserProfile
        fields = ("username", "email", "password1","password2","photo")
        labels = {"username":"Nombre completo", "email": "Correo","password1":"Ingrese contraseña","password2":"Confirme contraseña","photo":"Cargue una imagen"}

class AutheticateForm(forms.ModelForm):

    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data["email"]
        password = self.cleaned_date["password"]

        if not authenticate(email=email, password=password):
            raise forms.ValidationError("El email o la contraseña son incorrectos")