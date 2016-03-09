from django.conf.urls import patterns, include, url
from networkinstitute import views as networkinstitute_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', auth_views.login, {'template_name': 'login.html'}, name="socialweb_login"),
	url(r'^$', auth_views.logout, {'next_page': 'socialweb_home'}, name="socialweb_logout")
]