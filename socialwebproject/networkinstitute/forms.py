from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, ProjectOwner, Project, Faculty, Status

class CustomUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)
        #del self.fields['username']

    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name",)

class CustomUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(CustomUserChangeForm, self).__init__(*args, **kargs)

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name",)

class ProjectOwnerCreationForm(UserCreationForm):

    def __init__(self, *args, **kargs):
        super(ProjectOwnerCreationForm, self).__init__(*args, **kargs)

    class Meta:
        model = ProjectOwner
        fields = ("member",)

class ProjectOwnerChangeForm(UserChangeForm):

    def __init__(self, *args, **kargs):
        super(ProjectOwnerChangeForm, self).__init__(*args, **kargs)

    class Meta:
        model = ProjectOwner
        fields = ("member",)

class FacultyCreationForm(UserCreationForm):

    def __init__(self, *args, **kargs):
        super(FacultyCreationForm, self).__init__(*args, **kargs)

    class Meta:
        model = Faculty
        fields = ("name",)

class FacultyChangeForm(UserChangeForm):

    def __init__(self, *args, **kargs):
        super(FacultyChangeForm, self).__init__(*args, **kargs)
        #del self.fields['username']

    class Meta:
        model = Faculty
        fields = ("name",)

class ProjectCreationForm(UserCreationForm):

    def __init__(self, *args, **kargs):
        super(ProjectCreationForm, self).__init__(*args, **kargs)

    class Meta:
        model = Project
        fields = ("owner", "name", "description", "deadline")

class ProjectChangeForm(UserChangeForm):

    def __init__(self, *args, **kargs):
        super(ProjectChangeForm, self).__init__(*args, **kargs)

    class Meta:
        model = Project
        fields = ("owner", "name", "description", "deadline")

class StatusCreationForm(UserCreationForm):

    def __init__(self, *args, **kargs):
        super(StatusCreationForm, self).__init__(*args, **kargs)

    class Meta:
        model = Status
        fields = ("status", "project", "member")

class StatusChangeForm(UserChangeForm):

    def __init__(self, *args, **kargs):
        super(StatusChangeForm, self).__init__(*args, **kargs)

    class Meta:
        model = Status
        fields = ("status", "project", "member")