from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from networkinstitute.models import CustomUser, ProjectOwner, Project, Faculty

# Create your views here.


@login_required
def home(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projectdetails/home.html', {'project': project})