from django.forms import ModelForm
from networkinstitute.models import Project, ProjectOwner

class ProjectOwnerForm(ModelForm):
	class Meta:
		model = ProjectOwner
		fields = ['member',]

class ProjectForm(ModelForm):
	class Meta:
		model = Project
		fields = ['name', 'faculties', 'description', 'deadline']