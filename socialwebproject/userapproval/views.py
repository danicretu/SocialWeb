from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

from networkinstitute.models import CustomUser, ProjectOwner, Project, Faculty, Status

# Create your views here.

@csrf_protect
@login_required
def home(request, pk):
    project = get_object_or_404(Project, pk=pk)
    members = project.members.all()

    if request.method == "POST":
        for m in members:
            approve = "approve"+str(m.pk)
            decline = "decline"+str(m.pk)
        if request.POST.get(approve):
            s = Status.objects.get(project=project, member=m)
            s.status = 'A'
            #s.save()
            messages.success(request, 'You have approved the user!')
            context = {'project': project}
            return render(request, 'userapproval/home.html', context)
        if request.POST.get(decline):
            s = Status.objects.get(project=project, member=m)
            s.status = 'D'
            #s.save()
            messages.success(request, 'You have declined the user!')
            context = {'project': project,}
            return render(request, 'userapproval/home.html', context)

    context = {'project': project}
    return render(request, 'userapproval/home.html', context)