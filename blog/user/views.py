from django.shortcuts import render,HttpResponse

def register(request):
    return render(request,"register.html")
def loginUser(request):
    return HttpResponse("giriş yap")
def logout(request):
    return HttpResponse("çıkış yap")