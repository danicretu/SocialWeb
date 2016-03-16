from django.conf.urls import patterns, include, url
from visualisation import views as visualisation_views

urlpatterns = [
    url(r'^$', visualisation_views.home, name="visualisation_home")
]