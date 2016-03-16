from django.conf.urls import patterns, include, url
from myownedprojects import views as myownedprojects_views

urlpatterns = [
    url(r'^$', myownedprojects_views.home, name="myownedprojects_home"),
    url(r'^deadline-down', myownedprojects_views.deadlinedown, name="myownedprojects_deadline_down"),
    url(r'^deadline-up', myownedprojects_views.deadlineup, name="myownedprojects_deadline_up"),
    url(r'^az', myownedprojects_views.az, name="myownedprojects_az"),
    url(r'^za', myownedprojects_views.za, name="myownedprojects_za")
]