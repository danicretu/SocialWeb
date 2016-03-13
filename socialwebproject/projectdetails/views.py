from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from networkinstitute.models import CustomUser, ProjectOwner, Project, Faculty, Status

# Create your views here.


@login_required
def home(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        member = request.user
        project = Project.objects.get(pk=pk)
        project.members.add(member)
        project.save()
        status = Status.objects.create_status(project, member)
        status.save()
        messages.success(request, 'You have successfully applied for this project!')
    return render(request, 'projectdetails/home.html', {'project': project})