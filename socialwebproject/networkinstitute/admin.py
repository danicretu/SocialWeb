from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import AdminSite
from .models import CustomUser, ProjectOwner, Project, Faculty
from .forms import CustomUserChangeForm, CustomUserCreationForm

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

admin_site = MyAdminSite(name='admin')
admin_site.register(CustomUser, CustomUserAdmin)
admin_site.register(ProjectOwner)
admin_site.register(Project)
admin_site.register(Faculty)