from django.shortcuts import redirect, render
from .models import *
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import RegistroForm
from django.contrib.auth import login, authenticate


def index(request):
    return render(request, "index.html",{})

class Register(CreateView):
    model = UserProfile
    template_name = "register.html"
    form_class = RegistroForm 
    sucess_url = 'index'
    
class Login(LoginView):
    template_name = 'sing_in.html'
    
    def form_valid(self, form):
        print("me cago en la puta")
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')

    

