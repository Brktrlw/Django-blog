from django.shortcuts import render,redirect
from .forms import ArticleForm
from django.contrib import messages
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def dashboard(request):
    return render(request,"dashboard.html")

def addArticle(request):
    form=ArticleForm(request.POST or None)
    if form.is_valid():
        article=form.save(commit=False)
        article.author=request.user
        article.save()
        #title = form.cleaned_data.get("title")
        #content = form.cleaned_data.get("content")
        messages.success(request,"Makale başarıyla kayıt edildi.")
        return redirect("index")
    return render(request,"dashboard.html")