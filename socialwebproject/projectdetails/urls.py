from django.conf.urls import patterns, include, url
from projectdetails import views as projectdetails_views

urlpatterns = [
    
       url(r'^(?P<pk>\d+)/$', projectdetails_views.home, name='projectdetails_home'),
]