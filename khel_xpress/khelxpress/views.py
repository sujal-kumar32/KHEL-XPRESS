from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import requests
from django.http import JsonResponse


def home(request):

    return render(request, 'home.html')


def organize_view(request):
    return render(request, "organize.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('/')  
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login")

    return render(request, "login.html")


def register_view(request):
    if request.method == "POST":
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")

        
        username = f"{first_name}{last_name}".lower()

        if not first_name or not last_name or not email or not password:
            messages.error(request, "All fields are required.")
            return redirect("login")
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken. Try a different one.")
            return redirect("login")




        
   
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

  

  
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Registration successful! You are now logged in.")
            return redirect("/")  

    return render(request, "register.html")
       
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('/')



        

