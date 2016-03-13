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
    statuses = Status.objects.filter(project=project)

    if request.method == "POST":
        for m in members:
            approve = "approve"+str(m.pk)
            decline = "decline"+str(m.pk)
        if request.POST.get(approve):
            for s in statuses:
                #if s.member_id == int(approve[-1:]):
                            s.status = 'A'
                            break
            messages.success(request, 'You have approved the user!')
            context = {'project': project}
            return render(request, 'userapproval/home.html', context)
        if request.POST.get(decline):
            for s in statuses:
                if s.member_id == int(approve[-1:]):
                            s.status = 'D'
                            break
            messages.success(request, 'You have declined the user!')
            context = {'project': project,}
            return render(request, 'userapproval/home.html', context)

    context = {'project': project}
    return render(request, 'userapproval/home.html', context)