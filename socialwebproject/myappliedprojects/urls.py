from django.conf.urls import patterns, include, url
from myappliedprojects import views as myappliedprojects_views

urlpatterns = [
    url(r'^$', myappliedprojects_views.home, name="myappliedprojects_home")
]