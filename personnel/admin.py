from django.contrib import admin
from .models import PersonnelFile, Skill, PersonnelSkill, Species, Career, Talent, Weapon, Armor, Gear


@admin.register(PersonnelFile)
class PersonnelFileAdmin(admin.ModelAdmin):
    list_display = ['name', 'callsign', 'species', 'career', 'status']
    list_filter = ['status', 'species', 'career']
    search_fields = ['name', 'callsign', 'background']
    filter_horizontal = ['weapons', 'armor', 'gear', 'talents']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'characteristic', 'category']
    list_filter = ['category', 'characteristic']


@admin.register(PersonnelSkill)
class PersonnelSkillAdmin(admin.ModelAdmin):
    list_display = ['personnel', 'skill', 'rank', 'is_career']
    list_filter = ['is_career']


@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ['name', 'homeworld']


@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Talent)
class TalentAdmin(admin.ModelAdmin):
    list_display = ['name', 'rank', 'activation']


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ['name', 'damage', 'crit', 'range', 'encumbrance']


@admin.register(Armor)
class ArmorAdmin(admin.ModelAdmin):
    list_display = ['name', 'soak', 'defense', 'encumbrance']


@admin.register(Gear)
class GearAdmin(admin.ModelAdmin):
    list_display = ['name', 'encumbrance', 'rarity']
