from django.conf.urls import patterns, include, url
from userprofile import views as userprofile_views

urlpatterns = [
    url(r'^home$', userprofile_views.home, name="userprofile_home")
]