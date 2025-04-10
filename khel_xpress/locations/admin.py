from django.contrib import admin

# Register your models here.
from .models import State, District

class DistrictInline(admin.TabularInline):  # Or use StackedInline
    model = District
    extra = 1  # How many empty forms to show for adding new districts

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [DistrictInline]  # Show related districts inline

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')
    search_fields = ('name', 'state__name')
    list_filter = ('state',)