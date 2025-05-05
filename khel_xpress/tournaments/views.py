from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TournamentForm
from .models import Tournament


def register_tournament(request):
    if request.method == 'POST':
        post_data = request.POST.copy()  # Make the POST data mutable
        state_id = request.POST.get("state_id")
        state_name = request.POST.get("state_name")
        district_id = request.POST.get("district_id")
        district_name = request.POST.get("district_name")
        

        # Save the data to the database
        Tournament.objects.create(
            state_id=state_id,
            state_name=state_name,
            district_id=district_id,
            district_name=district_name,
            
            # Add other fields as needed
        )

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



