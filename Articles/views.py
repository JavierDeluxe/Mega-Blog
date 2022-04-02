from django.shortcuts import redirect, render
from tomlkit import comment
from .models import *
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import ArticleForm, RegistroForm
from django.contrib.auth import logout
from django.db.models import Q


def index(request):
    articles = Article.objects.all()
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

def watch_articulo(request, id):
    comments = Comment.objects.filter(publicacion_fk=id)
    sub_comments = Comment_second_level.objects.filter(comentario_fk = comments)
    article = Article.objects.get(pk=id)
    like = user_gave_like(request,id)
    return render(request,"article_section.html",{"article": article,"like":like,"comments":comments})

def remove_article(request, id):
    article = Article.objects.get(pk=id)
    article.delete()
    return index(request)

def user_gave_like(request, id):
    if not request.user.is_authenticated:
        return False
    else:
        article = Article.objects.get(pk=id)
        user = request.user
        exists = Hearts.objects.filter(Q(Q(author=user) & Q(article=article)))
        return len(exists) > 0 

def edit_article(request, id):
    article = Article.objects.get(pk=id)
    if request.method == 'POST':
        new_title = request.POST['title']
        new_open_mouth = request.POST['open_mouths']
        new_text = request.POST['text']
        new_image = request.FILES['image']
        article.title = new_title
        article.text = new_text
        article.open_mouths = new_open_mouth
        article.image = new_image
        article.save(update_fields=['title','open_mouths','text','image'])
        like = user_gave_like(request,id)
        return render(request,"article_section.html",{"article":article,"like":like})
    return render(request,"edit_article.html",{"article":article})

def like_article(request, id):
    article = Article.objects.get(pk=id)
    comments = Comment.objects.filter(publicacion_fk=id)
    user = request.user
    if request.method == 'GET':
        article = Article.objects.get(pk=id)
        user = UserProfile.objects.get(pk=user.id)
        exists = Hearts.objects.filter(Q(Q(author=user) & Q(article=article)))
        like = len(exists) > 0 
        if len(exists) == 0:
            exists = Hearts(author = user, article=article)
            exists.save()
            article.hearts_amount = article.hearts_amount + 1 
            article.save()
            like = True
    return render(request, "article_section.html",{"article":article,"like":like,"comments":comments})

def dislike_article(request, id):
    article = Article.objects.get(pk=id)
    comments = Comment.objects.filter(publicacion_fk=id)
    user = request.user
    print(user,article)
    exists = Hearts.objects.filter(Q(Q(author=user) & Q(article=article)))
    like = len(exists) > 0 
    if len(exists) > 0:
        exists.delete()
        article.hearts_amount = article.hearts_amount - 1 
        article.save()
        like = len(exists) > 0 
    return render(request, "article_section.html",{"article":article,"like":like,"comments":comments})


def comment_article(request,id):
    article = Article.objects.get(pk=id)
    user = request.user
    text = request.POST['text']
    print(id)
    if text is not "" and request.method == "POST":
        print("entro")
        comment = Comment(author_fk=user,text=text,publicacion_fk=article)
        comment.save()
    return watch_articulo(request,id)

def sub_comment(request,id):
    comment = Comment_second_level.objects.get(pk=id)
    user = request.user
    text = request.POST['text']
    if text is not "" and request.method == "POST":
        sub_comment = Comment_second_level(author_fk=user,text=text,comentario_fk=comment)
        sub_comment.save()
        print(comment,user,text)
    return watch_articulo(request,id)