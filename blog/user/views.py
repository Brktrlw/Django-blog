from django.shortcuts import render,HttpResponse,redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
def register(request):
    form =RegisterForm(request.POST or None)
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
        return render(request,"register.html")







def loginUser(request):
    return render(request,"login.html")
def logout(request):
    return HttpResponse("çıkış yap")