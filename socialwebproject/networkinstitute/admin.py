from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import AdminSite
from .models import CustomUser, ProjectOwner, Project, Faculty
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .forms import ProjectOwnerChangeForm, ProjectOwnerCreationForm
from .forms import ProjectChangeForm, ProjectCreationForm
from .forms import FacultyChangeForm, FacultyCreationForm

# Register your models here
class MyAdminSite(AdminSite):
	site_header = 'Network Institute administration'

class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference the removed 'username' field
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', "facebook", "twitter")}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ('email', 'first_name', 'last_name', "facebook", "twitter", 'is_staff')
    list_filter = ('date_joined',)
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ()

class ProjectOwnerAdmin(UserAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference the removed 'username' field
    fieldsets = (
        (None, {'fields': ('member', 'project_name')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('member', 'project_name')}
        ),
    )
    readonly_fields = ('project_name',)
    form = ProjectOwnerChangeForm
    add_form = ProjectOwnerCreationForm
    list_display = ('member', 'project_name')
    list_filter = ()
    search_fields = ('member',)
    ordering = ('member',)
    filter_horizontal = ()

    def project_name(self, obj):
        projects = obj.project_set.all()
        names = []
        for p in projects:
            names.append(p.name)
        return names

class FacultyAdmin(UserAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference the removed 'username' field
    fieldsets = (
        (None, {'fields': ('name',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name')}
        ),
    )
    form = FacultyChangeForm
    add_form = FacultyCreationForm
    list_display = ('name',)
    list_filter = ()
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()

class ProjectAdmin(UserAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference the removed 'username' field
    fieldsets = (
        (None, {'fields': ('owner', 'members', 'faculties',)}),
        (_('Personal info'), {'fields': ('name', 'description', 'deadline')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('owner', 'members', 'faculties',)}
        ),
    )
    form = ProjectChangeForm
    add_form = ProjectCreationForm
    list_display = ('owner', 'name', 'description', 'deadline')
    list_filter = ()
    search_fields = ('name', 'description', 'deadline')
    ordering = ('owner',)
    filter_horizontal = ()

admin_site = MyAdminSite(name='admin')
admin_site.register(CustomUser, CustomUserAdmin)
admin_site.register(ProjectOwner, ProjectOwnerAdmin)
admin_site.register(Project, ProjectAdmin)
admin_site.register(Faculty, FacultyAdmin)