from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from networkinstitute.models import CustomUser, ProjectOwner, Project, Faculty

# Create your views here.
@login_required
def home(request):
	member = request.user
	projects = list()
	for p in Project.objects.all():
		for m in p.members.all():
			if m == member and p.status == 'O':
				projects.append(p)
	if projects.count > 0:
		context = {'projects': projects}
		return render(request, "myappliedprojects/home.html", context)
	return render(request, "myappliedprojects/home.html")