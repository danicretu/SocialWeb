from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import connection, transaction

from networkinstitute.models import CustomUser
from networkinstitute.models import ProjectOwner
from networkinstitute.models import Project

from .forms import NewProjectForm

# Create your views here.
@login_required
def home(request):
	if request.method == 'POST':
		userid = request.user.id
		#cursor = connection.cursor()
		#cursor.execute("SELECT * FROM Members WHERE id = %s", [userid])
		#member = cursor.fetchone()
		form = NewProjectForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('socialweb_home')
	else:
		form = NewProjectForm()
	return render(request, "newproject/home.html", {'form': form})