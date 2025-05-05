from django.contrib import admin

# Register your models here.

from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_picture', 'cover_picture')  # Fields to display in the admin list view
    search_fields = ('user__username',)  # Enable search by username
    list_filter = ('user',)  # Add filters for the user field