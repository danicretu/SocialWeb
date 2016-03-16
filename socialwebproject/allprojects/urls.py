from django.conf.urls import patterns, include, url
from allprojects import views as allprojects_views

urlpatterns = [
    url(r'^$', allprojects_views.home, name="allprojects_home"),
    url(r'^deadline-down', allprojects_views.deadlinedown, name="allprojects_deadline_down"),
    url(r'^deadline-up', allprojects_views.deadlineup, name="allprojects_deadline_up"),
    url(r'^az', allprojects_views.az, name="allprojects_az"),
    url(r'^za', allprojects_views.za, name="allprojects_za")
]
