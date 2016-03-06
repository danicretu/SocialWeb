from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	facebook = models.CharField(max_length=100, blank=True)
	twitter = models.CharField(max_length=100, blank=True)

	#def __str__(self):
	#	return "{0} vs {1}".format(self.first_player, self.second_player)

class ProjectOwner(models.Model):
	member = models.OneToOneField(Member, on_delete=models.CASCADE)

class Project(models.Model):
	owner = models.ForeignKey(ProjectOwner)
	members = models.ManyToManyField(Member)
	name = models.CharField(max_length=100)
	description = models.TextField()
	deadline = models.DateField()

class Faculty(models.Model):
	project = models.ForeignKey(Project)