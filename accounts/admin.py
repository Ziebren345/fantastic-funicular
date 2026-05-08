from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'callsign', 'role']
    list_filter = ['role']
    search_fields = ['user__username', 'user__email', 'callsign']
