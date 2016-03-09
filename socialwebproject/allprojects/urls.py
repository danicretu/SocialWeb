from django.conf.urls import patterns, include, url
from allprojects import views as allprojects_views

urlpatterns = [
    url(r'^$', allprojects_views.home, name="allprojects_home")
]