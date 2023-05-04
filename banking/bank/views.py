from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse, request
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView


def HomeView(request):
     return render(request,'home.html')


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")


def register(request):
    if request.method=='POST':
        username=request.POST['name']
        password=request.POST['password']
        cpassword=request.POST['confirm_password']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists")
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
            print("user created")
        else:
            messages.info("password not matches")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def new(request):
    return render(request,'new.html')

def form(request):
    if request.method=='POST':
        name=request.POST['name']
        dob=request.POST['first_name']
        age=request.POST['age']
        phone = request.POST['phone']
        email=request.POST['email']
        gender = request.POST['gridRadios']
        district = request.POST['district']
        branch = request.POST['branch']
        account_type = request.POST['account_type']
    return render(request,'form.html')
