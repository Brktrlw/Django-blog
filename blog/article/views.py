from django.shortcuts import render,redirect,get_object_or_404
from .forms import ArticleForm
from django.contrib import messages
from .models import Article
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

@login_required(login_url="user:login")
def dashboard(request): # Tüm makalelerin bulunduğu sayfa
    articles=Article.objects.filter(author=request.user)
    return render(request,"userArticles.html",{"articles":articles})

def errorPage(request):
    return render(request,"404page.html")

@login_required(login_url="user:login")
def articleDetail(request,id):
    article=Article.objects.filter(id=id).first()
    if article==None:
        return render(request,"404page.html")
    else:
        return render(request,"detailArticle.html",{"article":article})

def articleCategorie(request):
    return render(request,"articleCategories.html")

def redirectIndex(request):
    if request.method=="GET":
        return redirect("index")

@login_required(login_url="user:login")
def addArticle(request):
    if request.method == 'GET':
        return redirect("index")
    else:
        form=ArticleForm(request.POST,request.FILES or None)
        if form.is_valid():
            article=form.save(commit=False)
            article.author=request.user
            article.save()
            #title = form.cleaned_data.get("title")
            #content = form.cleaned_data.get("content")
            messages.success(request,"Makale başarıyla kayıt edildi.")
            return redirect("index")
    return render(request,"dashboard.html")

@login_required(login_url="user:login")
def updateArticle(request,id):
    article=get_object_or_404(Article,id=id)
    form=ArticleForm(request.POST or None,request.FILES or None,instance=article)
    if form.is_valid():
        article=form.save()
        article.author=request.user
        article.save()
        return redirect("index")
    return render(request,"updateArticle.html",{"form":form})

@login_required(login_url="user:login")
def deleteArticle(request,id):
    article=get_object_or_404(Article,id=id)
    article.delete()
    messages.success(request,"Makale başarıyla silindi")
    return redirect("article:dashboard")

def categorie(request,id):
    articles=Article.objects.filter(Atype_id=id)
    return render(request,"articlesCAT.html",{"articles":articles})