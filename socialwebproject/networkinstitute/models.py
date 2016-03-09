from __future__ import unicode_literals

from django.db import models
from django.utils.http import urlquote
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _

# Create your models here.
PROJECT_STATUS_CHOICES = (
	('O', 'Operative'),
	('A', 'Accepted'),
	('D', 'Declined')
)

class CustomUserManager(BaseUserManager):
	def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
		"""
		Creates and saves a User with the given email and password.
		"""
		now = timezone.now()
		if not email:
			raise ValueError('The given email must be set')
		email = self.normalize_email(email)

		user = self.model(email=email,
							is_staff=is_staff, is_active=True,
							is_superuser=is_superuser, last_login=now,
							date_joined=now, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, password=None, **extra_fields):
		return self._create_user(email, password, False, False, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):
		return self._create_user(email, password, True, True, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField(max_length=254, unique=True)
	facebook = models.CharField(max_length=100, blank=True, unique=True)
	twitter = models.CharField(max_length=100, blank=True, unique=True)
	is_staff = models.BooleanField(_('staff status'), default=False,
		help_text=_('Designates whether the user can log into this admin '
					'site.'))
	is_active = models.BooleanField(_('active'), default=True,
		help_text=_('Designates whether this user should be treated as '
					'active. Unselect this instead of deleting accounts.'))
	date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name']

	objects = CustomUserManager()

	class Meta:
		verbose_name = _('user')
		verbose_name_plural = _('users')

	def get_absolute_url(self):
		return "/users/%s/" % urlquote(self.email)

	def get_full_name(self):
		"""
		Returns the first_name plus the last_name, with a space in between.
		"""
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip()

	def get_short_name(self):
		"Returns the short name for the user."
		return self.first_name

	def email_user(self, subject, message, from_email=None):
		"""
		Sends an email to this User.
		"""
		send_mail(subject, message, from_email, [self.email])

	def __str__(self):
		return "{0}".format(self.get_full_name())

class ProjectOwner(models.Model):
	member = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

class Project(models.Model):
	owner = models.OneToOneField(ProjectOwner, on_delete=models.CASCADE)
	members = models.ManyToManyField(CustomUser, related_name="members")
	name = models.CharField(max_length=100)
	description = models.TextField(help_text="Please provide a description, be sure to mention skills required, number of jobs available etc.")
	deadline = models.DateField(help_text="Please state the last date for applying to the project")
	status = models.CharField(max_length=1, default='O',
		choices=PROJECT_STATUS_CHOICES)

class Faculty(models.Model):
	project = models.ForeignKey(Project)