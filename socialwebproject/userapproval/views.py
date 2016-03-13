from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

from networkinstitute.models import CustomUser, ProjectOwner, Project, Faculty, Status

# Create your views here.
import logging
logger = logging.getLogger(__name__)

def myfunction():
    logger.debug("this is a debug message!")

def myotherfunction():
    logger.error("this is an error message!!")

@csrf_protect
@login_required
def home(request, pk):
    project = get_object_or_404(Project, pk=pk)
    members = project.members.all()
    appr = Status.objects.filter(status='A')
    decl = Status.objects.filter(status='D')

    if request.method == "POST":
        for m in members:
            approve = "approve"+str(m.pk)
            decline = "decline"+str(m.pk)
            if request.POST.get(approve):
                pk = int(approve[7:])
                member = CustomUser.objects.get(pk=pk)
                s = Status.objects.get(project=project, member=member)
                s.status = 'A'
                s.save()
                appr = Status.objects.filter(status='A')
                messages.success(request, 'You have approved the user!')
                context = {'project': project, 'appr': appr, 'decl': decl}
                return render(request, 'userapproval/home.html', context)
            if request.POST.get(decline):
                pk = int(decline[7:])
                member = CustomUser.objects.get(pk=pk)
                s = Status.objects.get(project=project, member=member)
                s.status = 'D'
                s.save()
                decl = Status.objects.filter(status='D')
                messages.success(request, 'You have declined the user!')
                context = {'project': project, 'appr': appr, 'decl': decl}
                return render(request, 'userapproval/home.html', context)

    context = {'project': project, 'appr': appr, 'decl': decl}
    return render(request, 'userapproval/home.html', context)