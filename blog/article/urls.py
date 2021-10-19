from django.contrib import admin
from django.urls import path
from article import views
from . import views
app_name="article"
urlpatterns = [
    path("dashboard/",views.dashboard,name="dashboard"),
]
