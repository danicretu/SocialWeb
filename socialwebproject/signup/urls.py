from django.conf.urls import patterns, include, url
from signup import views as signup_views

urlpatterns = [
    url(r'^$', signup_views.home, name="signup_home")
]