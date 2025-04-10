from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TournamentForm
from .models import Tournament

def register_tournament(request):
    if request.method == 'POST':
        post_data = request.POST.copy()  # Make the POST data mutable

        game_type = post_data.get('game_type')

        # Clear the irrelevant game field
        if game_type == 'sports':
            post_data['esports_game'] = ''
        elif game_type == 'esports':
            post_data['sports_game'] = ''

        form = TournamentForm(post_data, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Tournament registered successfully!")
            return redirect('home')
    else:
        form = TournamentForm()
    return render(request, 'organize.html', {'form': form})



def home(request):
    sports_tournaments = Tournament.objects.filter(game_type='sports').order_by('-id')
    esports_tournaments = Tournament.objects.filter(game_type='esports').order_by('-id')

    return render(request, 'home.html', {
        'sports_tournaments': sports_tournaments,
        'esports_tournaments': esports_tournaments,
    })