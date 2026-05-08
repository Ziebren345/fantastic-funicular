from django.contrib import admin
from .models import Faction, Relation, RelationLog, Planet


class RelationLogInline(admin.TabularInline):
    model = RelationLog
    extra = 1


@admin.register(Faction)
class FactionAdmin(admin.ModelAdmin):
    list_display = ['name', 'homeworld', 'government', 'technology']
    list_filter = ['government', 'technology']
    search_fields = ['name', 'description']


@admin.register(Relation)
class RelationAdmin(admin.ModelAdmin):
    list_display = ['faction', 'level', 'trend', 'trade_active', 'military_treaty']
    list_filter = ['level', 'trade_active', 'military_treaty']
    inlines = [RelationLogInline]


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_display = ['name', 'sector', 'climate', 'resources', 'controlling_faction']
    list_filter = ['climate', 'resources']
    search_fields = ['name', 'sector', 'description']
