from django.forms import ModelForm
from networkinstitute.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'deadline', 'owner']