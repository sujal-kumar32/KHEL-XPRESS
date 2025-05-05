from django.contrib import admin
from .models import Tournament, Registration

# Inline for displaying registrations within the Tournament admin page
class RegistrationInline(admin.TabularInline):
    model = Registration
    extra = 0  # No extra empty forms

# Admin configuration for Tournament
@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('tournament_name', 'game_type', 'start_date', 'end_date')
    search_fields = ('tournament_name', 'game_type')
    list_filter = ('game_type', 'start_date')
    inlines = [RegistrationInline]  # Add the inline for registrations

# Admin configuration for Registration
@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('player_name', 'tournament', 'email', 'phone', 'registered_at')
    search_fields = ('player_name', 'email', 'tournament__tournament_name')
    list_filter = ('tournament', 'gender', 'registered_at')