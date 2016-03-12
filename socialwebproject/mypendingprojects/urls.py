from django.conf.urls import patterns, include, url
from mypendingprojects import views as mypendingprojects_views

urlpatterns = [

       url(r'^$', mypendingprojects_views.home, name='mypendingprojects_home'),
]