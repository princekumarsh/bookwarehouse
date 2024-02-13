from django.shortcuts import render,redirect,HttpResponse
from home.models import user,Books
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
# Create your views here.

def index(request):
    return render(request, "index.html")

def user_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            auth_login(request,user)
            return redirect('/dashboard')
        else:
            return redirect('/login')
        
    return render(request, "login.html")

def register(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        u = user(name=name, email=email, mobile=mobile, password=password)
        u.save()
        print("success")
    return render(request, "index.html")

def dashboard(request):
    # if request.user.is_anonymous:
    #     return redirect('/login')
    # else:
    #     return render(request, "index.html")

    books = Books.objects.all()
    return render(request, 'dashboard.html', {'books': books})

    # return render(request, "dashboard.html")

def addbook(request):
    if request.method=="POST":
        # image = request.POST.get('image')
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        b = Books(name=name, desc=desc)
        b.save()
        print("success")
        return redirect("/dashboard")
    return render(request, "addbook.html")

def user_logout(request):
    logout(request)
    return redirect('/index')
