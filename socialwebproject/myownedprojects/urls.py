from django.conf.urls import patterns, include, url
from myownedprojects import views as myownedprojects_views

urlpatterns = [
    url(r'^$', myownedprojects_views.home, name="myownedprojects_home")
]