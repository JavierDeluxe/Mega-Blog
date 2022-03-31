from django.db import models
from django.forms import CharField
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
    image = models.ImageField()
    date = models.DateField()
    hearts = models.IntegerField()

class Comment(models.Model):
    author_fk = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    publicacion_fk = models.ForeignKey(Article, on_delete=models.CASCADE)

class Comment_second_level(models.Model):
    author_fk = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    comentario_fk = models.ForeignKey(Comment, on_delete=models.CASCADE)

class Hearts(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    amount = models.IntegerField()
