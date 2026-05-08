from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Mission


@login_required
def mission_list(request):
    missions = Mission.objects.all().order_by('-created_at')
    return render(request, 'missions/mission_list.html', {'missions': missions})


@login_required
def mission_detail(request, pk):
    mission = get_object_or_404(Mission, pk=pk)
    return render(request, 'missions/mission_detail.html', {'mission': mission})


@login_required
def my_missions(request):
    try:
        agent = request.user.personnel_file
        missions = agent.missions.all()
    except:
        missions = Mission.objects.none()
    return render(request, 'missions/mission_list.html', {'missions': missions, 'my_missions': True})
