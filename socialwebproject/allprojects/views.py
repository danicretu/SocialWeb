from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from networkinstitute.models import CustomUser, ProjectOwner, Project, Faculty

# Create your views here.
@login_required
def home(request):
	projects = Project.objects.all()
	context = {'projects': projects}
	return render(request, "allprojects/home.html", context)