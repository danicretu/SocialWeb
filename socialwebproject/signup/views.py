from django.shortcuts import render, render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
from django.db import connection, transaction
from django.contrib import messages

from networkinstitute.models import CustomUser

from .forms import SignupForm

# Create your views here.
def home(request):
	if request.method == 'POST':
		form = SignupForm(data=request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.set_password(user.password)
			user.save()
			messages.success(request, 'You have successfully registered with the Network Institute!')
	else:
		form = SignupForm()
	return render(request, "signup/home.html", {'form':form})