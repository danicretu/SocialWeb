from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from networkinstitute.models import CustomUser, ProjectOwner, Project, Faculty

# Create your views here.
@login_required
def home(request):
	member = request.user
	owners = ProjectOwner.objects.all()
	if owners.count > 0:
		for o in owners:
			if o.member_id == member.id:
				owner = o
				projects = Project.objects.filter(owner=owner)
				context = {'projects': projects}
				return render(request, "myownedprojects/home.html", context)
	return render(request, "myownedprojects/home.html")

@login_required
def deadlinedown(request):
	member = request.user
	owners = ProjectOwner.objects.all()
	if owners.count > 0:
		for o in owners:
			if o.member_id == member.id:
				owner = o
				projects = Project.objects.filter(owner=owner).order_by('-deadline')
				context = {'projects': projects}
				return render(request, "myownedprojects/home.html", context)
	return render(request, "myownedprojects/home.html")

@login_required
def deadlineup(request):
	member = request.user
	owners = ProjectOwner.objects.all()
	if owners.count > 0:
		for o in owners:
			if o.member_id == member.id:
				owner = o
				projects = Project.objects.filter(owner=owner).order_by('deadline')
				context = {'projects': projects}
				return render(request, "myownedprojects/home.html", context)
	return render(request, "myownedprojects/home.html")

@login_required
def az(request):
	member = request.user
	owners = ProjectOwner.objects.all()
	if owners.count > 0:
		for o in owners:
			if o.member_id == member.id:
				owner = o
				projects = Project.objects.filter(owner=owner).order_by('name')
				context = {'projects': projects}
				return render(request, "myownedprojects/home.html", context)
	return render(request, "myownedprojects/home.html")

@login_required
def za(request):
	member = request.user
	owners = ProjectOwner.objects.all()
	if owners.count > 0:
		for o in owners:
			if o.member_id == member.id:
				owner = o
				projects = Project.objects.filter(owner=owner).order_by('-name')
				context = {'projects': projects}
				return render(request, "myownedprojects/home.html", context)
	return render(request, "myownedprojects/home.html")