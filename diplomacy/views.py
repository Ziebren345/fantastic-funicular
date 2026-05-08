from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Faction, Relation, Planet


@login_required
def faction_list(request):
    factions = Faction.objects.all().order_by('name')
    return render(request, 'diplomacy/faction_list.html', {'factions': factions})


@login_required
def faction_detail(request, pk):
    faction = get_object_or_404(Faction, pk=pk)
    relation = getattr(faction, 'relation', None)
    planets = faction.planets.all()
    return render(request, 'diplomacy/faction_detail.html', {
        'faction': faction,
        'relation': relation,
        'planets': planets,
    })


@login_required
def planet_list(request):
    planets = Planet.objects.all().order_by('name')
    return render(request, 'diplomacy/planet_list.html', {'planets': planets})


@login_required
def planet_detail(request, pk):
    planet = get_object_or_404(Planet, pk=pk)
    return render(request, 'diplomacy/planet_detail.html', {'planet': planet})
