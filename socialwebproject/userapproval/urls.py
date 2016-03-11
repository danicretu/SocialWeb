from django.conf.urls import patterns, include, url
from userapproval import views as userapproval_views

urlpatterns = [

       url(r'^(?P<pk>\d+)/$', userapproval_views.home, name='userapproval_home'),
]