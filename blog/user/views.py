from django.shortcuts import render,HttpResponse
from .forms import RegisterForm
from django.contrib.auth.models import User
def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            mail=form.cleaned_data.get("mail")
            password=form.cleaned_data.get("password")
            print(username,mail,password)
            newUser=User(username=username,email=mail)
            newUser.set_password(password)
            newUser.save()
            return render(request,"register.html")

    else:
        form = RegisterForm()
        context = {
            "form": form
        }
        return render(request, "register.html", context)






def loginUser(request):
    return HttpResponse("giriş yap")
def logout(request):
    return HttpResponse("çıkış yap")