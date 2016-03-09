from django.shortcuts import render, render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
from django.db import connection, transaction
from django.contrib import messages

from networkinstitute.models import CustomUser
from networkinstitute.models import ProjectOwner
from networkinstitute.models import Project
from networkinstitute.models import Faculty

from .forms import ProjectForm, ProjectOwnerForm

# Create your views here.
@login_required
def home(request):
	if request.method == 'POST':
		form = ProjectForm(data=request.POST)
		if form.is_valid():
			member = request.user
			owner = ProjectOwner.objects.create_user(member)
			project = form.save(commit=False)
			project.owner = owner
			project.save()
			messages.success(request, 'Project successfully created!')
	else:
		form = ProjectForm()
	return render(request, "newproject/home.html", {'form': form})