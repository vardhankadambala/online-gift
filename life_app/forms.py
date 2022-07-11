from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import cart,cart1
from django import forms

class UserReg(UserCreationForm):
	class Meta:
		model = User
		fields = ["first_name","last_name","email","username"]

class cartform(forms.ModelForm):
	class Meta:
		model = cart
		fields="__all__"


class cartform1(forms.ModelForm):
	class Meta:
		model = cart1
		fields="__all__"