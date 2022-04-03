from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class UserProfile(AbstractUser):
    photo = models.ImageField()
    
    def get_absolute_url(self):
        return reverse("articles:index")
    
class Article(models.Model):
    title = models.CharField(max_length=1000)
    author_fk = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    open_mouths = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    image = models.ImageField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    hearts_amount = models.IntegerField(default=0)
    
    def get_absolute_url(self):
        return reverse("articles:index")
    

class Comment(models.Model):
    author_fk = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    publicacion_fk = models.ForeignKey(Article, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

class Comment_second_level(models.Model):
    author_fk = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    comentario_fk = models.ForeignKey(Comment, on_delete=models.CASCADE)
    article_fk= models.ForeignKey(Article, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

class Hearts(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    
class Reactions_comments_1(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    like = models.BooleanField()
    dislike = models.BooleanField()
    
class Reactions_comments_2(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment_second_level, on_delete=models.CASCADE)
    like = models.BooleanField()
    dislike = models.BooleanField()
