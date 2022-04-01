from email.mime import image
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .models import Article, UserProfile


class RegistroForm(UserCreationForm):
  
    class Meta():
        model = UserProfile
        fields = ("username", "email", "password1","password2","photo")
        labels = {"username":"Nombre completo", "email": "Correo","password1":"Ingrese contraseña","password2":"Confirme contraseña","photo":"Cargue una imagen"}

class ArticleForm(forms.ModelForm):

    class Meta():
        model = Article
        fields = {
            "author_fk",
            "title",
            "text",
            "image",
        }

        labels = {
            "Autor: ": "author_fk",
            "Titulo del articulo: ": "title",
            "Contenido del articulo": "text",
            "Imagen":"image"
        }
