from django import forms
from django.forms import ModelForm, CharField, PasswordInput
from networkinstitute.models import CustomUser

class SignupForm(ModelForm):
	class Meta:
		password = forms.CharField(widget=forms.PasswordInput())
		model = CustomUser
		fields = ['first_name','last_name','email','password']
		widgets = {
			'password':forms.PasswordInput(),
		}
		#self.fields['password'].widget=forms.HiddenInput()
