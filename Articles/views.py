from django.shortcuts import render
from django.urls import reverse
from .models import *
from django.views.generic import CreateView
from .forms import RegistroForm

def index(request):
    return render(request, "index.html",{})

class Register(CreateView):
    model = UserProfile
    template_name = "register.html"
    form_class = RegistroForm 
    sucess_url= 'index'

