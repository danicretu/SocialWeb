from django.conf.urls import patterns, include, url
from newproject import views as newproject_views

urlpatterns = [
    url(r'^$', newproject_views.home, name="newproject_home")
]