from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django import forms

def home(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')
        user=authenticate(request,username,password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render(request,"todo/index.html")

def signin(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        print(pass1!=pass2,"your password not match")

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        elif User.objects.filter(email=email).exist():
            messages.warning(request,"email already exist")
            return redirect("signup")
        else:

            messages.success(request,"your account has successfully created")
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('signin')
        
            
    return render(request,"todo/signin.html")
def signup(request):
    return render(request,"todo/signup.html")
def LogoutPage(request):
    logout(request)
    return redirect('index.html')