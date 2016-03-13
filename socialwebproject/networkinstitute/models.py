from __future__ import unicode_literals

from django.db import models
from django.utils.http import urlquote
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from djchoices import DjangoChoices, ChoiceItem


# Create your models here.



class NullableCharField(models.CharField):
	"""
	Subclass of the CharField that allows empty strings to be stored as NULL.
	"""

	description = "CharField that stores NULL but returns ''."

	def from_db_value(self, value, expression, connection, contex):
		"""
		Gets value right out of the db and changes it if its ``None``.
		"""
		if value is None:
			return ''
		else:
			return value


	def to_python(self, value):
		"""
		Gets value right out of the db or an instance, and changes it if its ``None``.
		"""
		if isinstance(value, models.CharField):
			# If an instance, just return the instance.
			return value
		if value is None:
			# If db has NULL, convert it to ''.
			return ''

		# Otherwise, just return the value.
		return value

	def get_prep_value(self, value):
		"""
		Catches value right before sending to db.
		"""
		if (value is ''):
			# If Django tries to save an empty string, send the db None (NULL).
			return None
		else:
			# Otherwise, just pass the value.
			return value

class CustomUserManager(BaseUserManager):
	def _create_user(self, email, password,is_staff, is_superuser, **extra_fields):
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

	def check_status(self):
		return self.status_set.all()

class CustomUser(AbstractBaseUser, PermissionsMixin):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	username = models.CharField(max_length=50)
	email = models.EmailField(max_length=254, unique=True)
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

class ProjectOwnerManager(models.Manager):
	def _create_user(self, member):
		owner = self.model(member=member)
		owner.save(using=self._db)
		return owner

	def create_user(self, member):
		return self._create_user(member)

class ProjectOwner(models.Model):
	member = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

	objects = ProjectOwnerManager()

	def __str__(self):
		return "{0}".format(self.member.get_full_name())

class Faculty(models.Model):
	name = models.CharField(max_length=100, default="Faculty")

	def __str__(self):
		return "{0}".format(self.name)

class ProjectManager(models.Manager):
	def _create_project(self, owner, faculties, name, description, deadline):
		project = self.model(owner=owner, faculties=faculties, name=name, description=description, deadline=deadline)
		project.save(using=self._db)
		return project

	def create_project(self, owner, faculties, name, description, deadline):
		return self._create_project(owner, faculties, name, description, deadline)

class Project(models.Model):
	owner = models.ForeignKey(ProjectOwner, on_delete=models.CASCADE)
	members = models.ManyToManyField(CustomUser, related_name="members")
	faculties = models.ManyToManyField(Faculty, related_name="faculties",
									help_text="To select more faculties, hold ctrl for Windows or command for Mac")
	name = models.CharField(max_length=100)
	description = models.TextField(help_text="Please provide a description, be sure to mention skills required, number of jobs available etc.")
	deadline = models.DateField(help_text="Please state the last date for applying to the project as yyyy-mm-dd")

	objects = ProjectManager()

	def __str__(self):
		return "{0}".format(self.name)

class StatusManager(models.Manager):
	def _create_status(self, project, member):
		status = self.model(status='O', project=project, member=member)
		status.save(using=self._db)
		return status

	def create_status(self, project, member):
		return self._create_status(project, member)

class Status(models.Model):
	#Choices
	class StatusType(DjangoChoices):
		Operative = ChoiceItem('O')
		Approved = ChoiceItem('A')
		Declined = ChoiceItem('D')

	#Fields
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	member = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
	status = models.CharField(max_length=1, default='O', choices=StatusType.choices, validators=[StatusType.validator])

	objects = StatusManager()

	def __str__(self):
		return "{0}".format(self.project)