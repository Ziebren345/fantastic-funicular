from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import PersonnelFile


@login_required
def personnel_list(request):
    personnel = PersonnelFile.objects.all().order_by('name')
    return render(request, 'personnel/personnel_list.html', {'personnel': personnel})


@login_required
def personnel_detail(request, pk):
    agent = get_object_or_404(PersonnelFile, pk=pk)
    return render(request, 'personnel/personnel_detail.html', {'agent': agent})


@login_required
def my_personnel(request):
    try:
        agent = request.user.personnel_file
    except PersonnelFile.DoesNotExist:
        messages.warning(request, "No personnel file found. Contact a Game Master to create one.")
        return redirect('dashboard')
    return render(request, 'personnel/personnel_detail.html', {'agent': agent, 'my_profile': True})
