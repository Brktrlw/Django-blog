from django.shortcuts import render,redirect,get_object_or_404
from .forms import ArticleForm
from django.contrib import messages
from .models import Article

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def dashboard(request): # Tüm makalelerin bulunduğu sayfa
    articles=Article.objects.filter(author=request.user)
    return render(request,"userArticles.html",{"articles":articles})

def articleDetail(request,id):
    #article=Article.objects.filter(id=id).first()
    article=get_object_or_404(Article,id=id)
    return render(request,"detailArticle.html",{"article":article})

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