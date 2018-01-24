from django.contrib.auth.models import User
from django import forms
from .models import Board

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	# This is just info about class 
	class Meta:
		model = User
		fields = ['username', 'email', 'password']

class UserImageUpload(forms.ModelForm):

	class Meta:
		model = Board
		fields = ['header','content','file']
		widgets= {
			'header': forms.TextInput(attrs= {'size':67}),
			'content':forms.Textarea(attrs = {'cols':70, 'rows':20})
		}