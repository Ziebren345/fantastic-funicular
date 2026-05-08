from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import GearRequest
from .forms import GearRequestForm


@login_required
def gear_request_list(request):
    if request.user.profile.is_gm():
        requests = GearRequest.objects.all().order_by('-urgency', '-created_at')
    else:
        try:
            agent = request.user.personnel_file
            requests = GearRequest.objects.filter(requester=agent)
        except:
            requests = GearRequest.objects.none()
    return render(request, 'logistics/gear_list.html', {'requests': requests})


@login_required
def gear_request_create(request):
    try:
        agent = request.user.personnel_file
    except:
        messages.error(request, "No personnel file found. Contact a GM before requesting gear.")
        return redirect('dashboard')

    if request.method == 'POST':
        form = GearRequestForm(request.POST)
        if form.is_valid():
            gear_req = form.save(commit=False)
            gear_req.requester = agent
            gear_req.save()
            messages.success(request, "Gear request submitted for review.")
            return redirect('gear_request_list')
    else:
        form = GearRequestForm()
    return render(request, 'logistics/gear_form.html', {'form': form})


@login_required
def gear_request_detail(request, pk):
    gear_req = get_object_or_404(GearRequest, pk=pk)
    return render(request, 'logistics/gear_detail.html', {'request': gear_req})
