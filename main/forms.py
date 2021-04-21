from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import MyUser

class MyUserRegisterForm(forms.ModelForm):
	class Meta:
		model = MyUser
		fields = "__all__"


class RegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]
		widgets = {
			'username':forms.TextInput(attrs={'class':'form-control'}),
		}