from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from networkinstitute.models import CustomUser, ProjectOwner, Project, Faculty, Status

# Create your views here.
@login_required
def home(request):
	member = request.user
	projects = list()
	statuses = Status.objects.all()
	for p in Project.objects.all():
		for s in statuses:
			if s.project == p and s.member == member:
				if s.status == 'O':
					projects.append(p)
	if projects.count > 0:
		context = {'projects': projects}
		return render(request, "mypendingprojects/home.html", context)
	return render(request, "mypendingprojects/home.html")

@login_required
def deadlinedown(request):
	member = request.user
	projects = list()
	statuses = Status.objects.all()
	for p in Project.objects.order_by('-deadline'):
		for s in statuses:
			if s.project == p and s.member == member:
				if s.status == 'O':
					projects.append(p)
	if projects.count > 0:
		context = {'projects': projects}
		return render(request, "mypendingprojects/home.html", context)
	return render(request, "mypendingprojects/home.html")

@login_required
def deadlineup(request):
	member = request.user
	projects = list()
	statuses = Status.objects.all()
	for p in Project.objects.order_by('deadline'):
		for s in statuses:
			if s.project == p and s.member == member:
				if s.status == 'O':
					projects.append(p)
	if projects.count > 0:
		context = {'projects': projects}
		return render(request, "mypendingprojects/home.html", context)
	return render(request, "mypendingprojects/home.html")

@login_required
def az(request):
	member = request.user
	projects = list()
	statuses = Status.objects.all()
	for p in Project.objects.order_by('name'):
		for s in statuses:
			if s.project == p and s.member == member:
				if s.status == 'O':
					projects.append(p)
	if projects.count > 0:
		context = {'projects': projects}
		return render(request, "mypendingprojects/home.html", context)
	return render(request, "mypendingprojects/home.html")

@login_required
def za(request):
	member = request.user
	projects = list()
	statuses = Status.objects.all()
	for p in Project.objects.order_by('-name'):
		for s in statuses:
			if s.project == p and s.member == member:
				if s.status == 'O':
					projects.append(p)
	if projects.count > 0:
		context = {'projects': projects}
		return render(request, "mypendingprojects/home.html", context)
	return render(request, "mypendingprojects/home.html")