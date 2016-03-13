from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from networkinstitute.models import CustomUser

# Create your views here.
@login_required
def home(request):
	member = CustomUser.objects.get(id=request.user.id)
	full_name = member.get_full_name()
	email = member.email
	context = {'full_name': full_name,
				'email': email,}
	return render(request, "userprofile/home.html", context)