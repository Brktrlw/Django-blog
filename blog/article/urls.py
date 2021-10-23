from django.contrib import admin
from django.urls import path
from article import views
from . import views
app_name="article"
urlpatterns = [
    path("dashboard/",views.dashboard,name="dashboard"),
    path("",views.redirectIndex,name="redirectIndex"),
    path("addArticle/",views.addArticle,name="addArticle"),
    path("details/<int:id>", views.articleDetail, name="articleDetail"),
    path("details/", views.errorPage, name="errorPage"),
    path("update/<int:id>",views.updateArticle,name="updateArticle"),
    path("delete/<int:id>",views.deleteArticle,name="deleteArticle"),
    path("article-categorie/",views.articleCategorie,name="articleCategorie"),
    path("categorie/<int:id>", views.categorie, name="categorie"),
    path("comment/<int:id>",views.addComment,name="addComment")
]
