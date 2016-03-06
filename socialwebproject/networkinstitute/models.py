from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
PROJECT_STATUS_CHOICES = (
	('O', 'Operative'),
	('A', 'Accepted'),
	('D', 'Declined')
)

class Member(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	facebook = models.CharField(max_length=100, blank=True)
	twitter = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return "{0}".format(self.user.get_username())

class ProjectOwner(models.Model):
	member = models.OneToOneField(Member, on_delete=models.CASCADE)

class Project(models.Model):
	owner = models.OneToOneField(ProjectOwner, on_delete=models.CASCADE)
	members = models.ManyToManyField(Member)
	name = models.CharField(max_length=100)
	description = models.TextField()
	deadline = models.DateField()
	status = models.CharField(max_length=1, default='O',
		choices=PROJECT_STATUS_CHOICES)

class Faculty(models.Model):
	project = models.ForeignKey(Project)