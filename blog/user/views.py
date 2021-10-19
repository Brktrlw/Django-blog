from django.shortcuts import render,HttpResponse,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib.auth import logout as django_logout

from django.contrib import messages
def register(request):
    #form =RegisterForm(request.POST or None)
    form=RegisterForm(request.POST)
    if request.method=="POST":
        if form.is_valid():
            username=form.cleaned_data.get("username")
            mail=form.cleaned_data.get("mail")
            password=form.cleaned_data.get("password")
            newUser=User(username=username,email=mail)
            newUser.set_password(password)
            newUser.save()
            login(request,newUser)
            messages.success(request,"Başarıyla kayıt olundu")
            return redirect("index")
        else:
            messages.success(request,"Parolalar Eşleşmiyor")
            return render(request,"register.html")
    else:
        return render(request,"register.html")

def loginUser(request):
    form=LoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(username=username,password=password)
        if user is None:
            messages.warning(request,"Giriş bilgileriniz hatalıdır,lütfen tekrar deneyiniz.")
            return render(request,"login.html")
        else:
            messages.success(request,"Başarıyla giriş yaptınız")
            login(request,user)
            return redirect("index")
    else:
        return render(request,"login.html")

    #return render(request,"login.html")
def logout(request):
    django_logout(request)
    messages.success(request,"Başarıyla çıkış yaptınız")
    return redirect("index")