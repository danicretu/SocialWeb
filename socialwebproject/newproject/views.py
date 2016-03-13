from django.shortcuts import render, render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
from django.db import connection, transaction
from django.contrib import messages

from networkinstitute.models import CustomUser, ProjectOwner, Project, Faculty, Status

from .forms import ProjectForm, ProjectOwnerForm

# Create your views here.
@login_required
def home(request):
	if request.method == 'POST':
		form = ProjectForm(data=request.POST)
		if form.is_valid():
			member = request.user
			owners = ProjectOwner.objects.all()
			for o in owners:
				if o.member_id == member.id:
					owner = o
					break
				else:
					owner = ProjectOwner.objects.create_user(member)
			project = form.save(commit=False)
			project.owner = owner
			project.save()
			messages.success(request, 'You have successfully created a new project!')
	else:
		form = ProjectForm()
	return render(request, "newproject/home.html", {'form': form})