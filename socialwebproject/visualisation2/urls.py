from django.conf.urls import patterns, include, url
from visualisation2 import views as visualisation2_views

urlpatterns = [
    url(r'^$', visualisation2_views.home, name="visualisation2_home")
]