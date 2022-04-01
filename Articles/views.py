from django.shortcuts import redirect, render
from .models import *
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import ArticleForm, RegistroForm
from django.contrib.auth import logout


def index(request):
    articles = Article.objects.all()
    article_rows = 3
    return render(request, "index.html",{"articles":articles,"range":range(0,3)})

class Register(CreateView):
    model = UserProfile
    template_name = "register.html"
    form_class = RegistroForm 
    sucess_url = 'index'
    
class Login(LoginView):
    template_name = 'sing_in.html'

class LogOut(LogoutView):
    pass
    
class RegisterArticle(CreateView):
    model = Article
    template_name = "new_article.html"
    form_class = ArticleForm
    sucess_url = 'index'
    
    def form_valid(self, form):
        print(self.fields)
        return super().form_valid(form)

def watch_articulo(request, id):
    article = Article.objects.get(pk=id)
    print(article)
    return render(request,"article_section.html",{"article": article})

