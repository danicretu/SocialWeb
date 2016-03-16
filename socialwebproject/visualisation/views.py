from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount

# Create your views here.

def home(request):

	memberGoogle = SocialAccount.objects.filter(provider="google")
	memberFacebook =SocialAccount.objects.filter(provider="facebook")
	memberLinkedin = SocialAccount.objects.filter(provider="linkedin")

	context = {'google': "Google",
				'googleCount': len(memberGoogle),
				'facebook': "Facebook",
				'facebookCount': len(memberFacebook),
				'linkedin': "LinkedIn",
				'linkedinCount': len(memberLinkedin),
	}

	return render(request, "visualisation/home.html", context)