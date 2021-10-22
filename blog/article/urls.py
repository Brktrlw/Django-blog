from django.contrib import admin
from django.urls import path
from article import views
from . import views
app_name="article"
urlpatterns = [
    path("dashboard/",views.dashboard,name="dashboard"),
    path("addArticle/",views.addArticle,name="addArticle"),
    path("details/<int:id>", views.articleDetail, name="articleDetail"),
    path("create-article/",views.createArticle,name="createArticle")
]
