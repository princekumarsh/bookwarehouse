from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
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

def updatebook(request, id):
    # if request.method=="POST":
    #     # image = request.POST.get('image')
    #     name = request.POST.get('name')
    #     desc = request.POST.get('desc')
    #     b = Books(name=name, desc=desc)
    #     b.save()
    #     print("success")
    #     return redirect("/dashboard")

    book = get_object_or_404(Books, id=id)

    if request.method == 'POST':
        # image = request.POST.get('image')
        book.name = request.POST.get('name')
        book.desc = request.POST.get('desc')
        # b = Books(name=name, desc=desc)
        book.save()
        print("success")
        return redirect("/dashboard")
    else:
        # If it's a GET request, pre-populate the form with old values
        context = {
            'book':book
            # 'id': book.id,
            # 'name': book.name,
            # 'desc': book.desc,
        }
        return render(request, 'updatebook.html', context)

def deletebook(request, id):
    Books.objects.filter(id=id).delete()
    return redirect("/dashboard")

def user_logout(request):
    logout(request)
    return redirect('/index')
