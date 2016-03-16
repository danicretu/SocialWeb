from django.conf.urls import patterns, include, url
from myappliedprojects import views as myappliedprojects_views

urlpatterns = [
    url(r'^$', myappliedprojects_views.home, name="myappliedprojects_home"),
    url(r'^deadline-down', myappliedprojects_views.deadlinedown, name="myappliedprojects_deadline_down"),
    url(r'^deadline-up', myappliedprojects_views.deadlineup, name="myappliedprojects_deadline_up"),
    url(r'^az', myappliedprojects_views.az, name="myappliedprojects_az"),
    url(r'^za', myappliedprojects_views.za, name="myappliedprojects_za")
]