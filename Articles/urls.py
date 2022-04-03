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
    path("ver_articulo/<int:id>",watch_articulo, name="watch_article"),
    path("ver_articulo/<int:id>/editar_articulo/",edit_article,name="edit_article"),
    path("<int:id>/eliminar_articulo/",remove_article,name="remove_article"),
    path("ver_articulo/<int:id>/like/",like_article,name="like_article"),
    path("ver_articulo/<int:id>/dislike/",dislike_article,name="dislike_article"),
    path("ver_articulo/<int:id>/comment/",comment_article,name="comment_article"),
    path("ver_articulo/<int:id>/subcomment_article",sub_comment,name="subcomment"),
    path("my_articles/",my_articles,name="my_articles"),
    path("ver_articulo/<int:id>/like_comment/<int:id2>/<int:id3>",like_comment,name="like_comment"),
    path("ver_articulo/<int:id>/dislike_comment/<int:id2>/<int:id3>",dislike_comment,name="dislike_comment"),
]


