from django.shortcuts import render,redirect,get_object_or_404,reverse
from .forms import ArticleForm
from django.contrib import messages
from .models import Article,Comment
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

def articleDetail(request,id):
    article=Article.objects.filter(id=id).first()
    comments=article.getComments.all()


    if article==None:
        return render(request,"404page.html")
    else:
        return render(request,"detailArticle.html",{"article":article,"comments":comments})

def articleCategorie(request):
    return render(request,"articleCategories.html")

def redirectIndex(request):
    if request.method=="GET":
        return render("index")

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
    keyword=request.GET.get("keyword")
    if keyword:
        articles=Article.objects.filter(title__contains=keyword,Atype_id=id)
        return render(request,"articlesCAT.html",{"articles":articles})
    else:
        articles=Article.objects.filter(Atype_id=id)
        return render(request,"articlesCAT.html",{"articles":articles})
@login_required
def addComment(request,id):
    article=get_object_or_404(Article,id=id)
    if request.method=="POST":
        commentContent=request.POST.get("commentContent")
        print(commentContent,"**************************")
        newComment=Comment(commentContent=commentContent,commentAuthor_id=request.user.id)
        newComment.article=article
        newComment.save()
        return redirect("/articles/details/"+str(id))
