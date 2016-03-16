from django.conf.urls import patterns, include, url
from mypendingprojects import views as mypendingprojects_views

urlpatterns = [
       url(r'^$', mypendingprojects_views.home, name='mypendingprojects_home'),
       url(r'^deadline-down', mypendingprojects_views.deadlinedown, name="mypendingprojects_deadline_down"),
       url(r'^deadline-up', mypendingprojects_views.deadlineup, name="mypendingprojects_deadline_up"),
       url(r'^az', mypendingprojects_views.az, name="mypendingprojects_az"),
       url(r'^za', mypendingprojects_views.za, name="mypendingprojects_za")
]