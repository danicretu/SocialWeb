from django.forms import ModelForm
from networkinstitute.models import Project

class NewProjectForm(ModelForm):
	class Meta:
		model = Project
		fields = ['name', 'description', 'deadline']