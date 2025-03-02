from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def home(request):

    return render(request, 'home.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('/')  # Change to your homepage URL
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

        # Combine First Name & Last Name to create a Username
        username = f"{first_name}{last_name}".lower()

        if not first_name or not last_name or not email or not password:
            messages.error(request, "All fields are required.")
            return redirect("login")
        
        # Check if user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken. Try a different one.")
            return redirect("login")



        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered. Try logging in.")
            return redirect("login")
        
        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

                # Auto-login after registration
        user = authenticate(request, username=username, password=password)

        # Auto-login after registration
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("/")  # Redirect to homepage

    return render(request, "register.html")
       
def logout_view(request):
    logout(request)
    return redirect('/') 
        
