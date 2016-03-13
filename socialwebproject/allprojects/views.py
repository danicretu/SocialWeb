from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from networkinstitute.models import CustomUser, ProjectOwner, Project, Faculty

# Create your views here.
@login_required
def home(request):
	member = request.user
	owners = ProjectOwner.objects.all()
	for o in owners:
		if o.member_id == member.id:
			owner = o
			projects = Project.objects.exclude(owner=owner)
			break
		else:
			projects = Project.objects.all()
	context = {'projects': projects}
	return render(request, "allprojects/home.html", context)