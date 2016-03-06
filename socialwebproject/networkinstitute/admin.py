from django.contrib import admin
from .models import Member, ProjectOwner, Project, Faculty

# Register your models here.
admin.site.register(Member)
admin.site.register(ProjectOwner)
admin.site.register(Project)
admin.site.register(Faculty)