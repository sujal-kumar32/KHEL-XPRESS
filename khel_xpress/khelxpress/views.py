from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.core.mail import send_mail
import json
import re
from tournaments.models import Tournament, Registration


 




def home(request):
    sports_tournaments = Tournament.objects.filter(game_type='sports').exclude(tournament_poster=None)
    esports_tournaments = Tournament.objects.filter(game_type='esports').exclude(tournament_poster=None)
    return render(request, 'home.html', {  'sports_tournaments': sports_tournaments,
        'esports_tournaments': esports_tournaments,})


def organize_view(request):
    return render(request, "organize.html")



def profile(request):
    return render(request, "profile.html")


def play_view(request):
        # Fetching all tournaments and categorizing them
    mixed_tournaments = Tournament.objects.filter(game_type__in=['sports', 'esports']).order_by('-start_date')[:5]
    upcoming_sports = Tournament.objects.filter(game_type='sports', start_date__gte='2025-04-28').order_by('start_date')[:5]
    show_esports = Tournament.objects.filter(game_type='esports').order_by('-start_date')[:5]

    return render(request, 'play.html', {
        'mixed_tournaments': mixed_tournaments,
        'upcoming_sports': upcoming_sports,
        'show_esports': show_esports,
    })

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




def subscribe(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get("email")

            # Validate email format
            email_pattern = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
            if not email or not re.match(email_pattern, email):
                return JsonResponse({"message": "Invalid email format!"}, status=400)

            # Sending confirmation email
            send_mail(
                "Subscription Successful",
                "Thank you for subscribing to our newsletter!",
                "sujalstark12345@gmail.com",  # Change this to your email
                [email],
                fail_silently=False,
            )

            return JsonResponse({"message": "Subscription successful! Check your email."})

        except Exception as e:
            print(f"DEBUG ERROR: {e}")  # Debug print to see error in terminal
            return JsonResponse({"message": f"Internal Error: {str(e)}"}, status=500)

    return JsonResponse({"message": "Invalid request"}, status=400)


def tournament_detail(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)
    return render(request, 'tournament_detail.html', {'tournament': tournament})

def register_tournament(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)
    # Add your registration logic here
    return render(request, 'register_tournament.html', {'tournament': tournament})


def submit_registration(request, tournament_id):
    if request.method == 'POST':
        # Fetch the tournament object
        tournament = get_object_or_404(Tournament, id=tournament_id)

        # Check if the user has already registered for this tournament
        existing_registration = Registration.objects.filter(tournament=tournament, email=request.user.email).exists()

        if existing_registration:
            # If the user has already registered, show a message
            messages.error(request, "You have already registered for this tournament.")
            return redirect('home')

        # Process the form data
        player_name = request.POST.get('player_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        team_name = request.POST.get('team_name', None)
        team_members = request.POST.get('team_members', None)
        additional_info = request.POST.get('additional_info', '')

        # Save the registration
        Registration.objects.create(
            tournament=tournament,
            player_name=player_name,
            email=email,
            phone=phone,
            age=age,
            gender=gender,
            team_name=team_name,
            team_members=team_members,
            additional_info=additional_info,
        )

        # Add a success message
        messages.success(request, f"Registration successful for {player_name} in {tournament.tournament_name}!")

        # Redirect to the home page
        return redirect('home')
    return redirect('register_tournament', tournament_id=tournament_id)