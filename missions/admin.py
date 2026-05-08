from django.contrib import admin
from .models import Mission, Objective


class ObjectiveInline(admin.TabularInline):
    model = Objective
    extra = 2


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ['codename', 'title', 'status', 'classification', 'threat_level', 'created_at']
    list_filter = ['status', 'classification', 'threat_level']
    search_fields = ['title', 'codename', 'briefing']
    filter_horizontal = ['assigned_personnel']
    inlines = [ObjectiveInline]


@admin.register(Objective)
class ObjectiveAdmin(admin.ModelAdmin):
    list_display = ['mission', 'order', 'description', 'is_primary', 'is_complete']
    list_filter = ['is_primary', 'is_complete']
