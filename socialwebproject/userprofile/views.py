from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from networkinstitute.models import Member

# Create your views here.
@login_required
def home(request):
	member = Member.objects.get(user=request.user)
	full_name = member.user.get_full_name()
	email = member.user.email
	facebook = member.facebook
	twitter = member.twitter
	context = {'full_name': full_name,
				'email': email,
				'facebook': facebook,
				'twitter': twitter}
	return render(request, "userprofile/home.html", context)