from django import forms

from .models import Client

import datetime

# class ClientForm(forms.ModelForm):
# 	class Meta:
# 		model = Client
# 		fields =('username', 'password')

class ClientForm(forms.ModelForm):
	class Meta:
		model = Client
		exclude =['created_at']

	username = forms.CharField(label=False,widget=forms.TextInput(attrs={'placeholder':'Adresse e-mail ou numéro de tél.'}))
	password = forms.CharField(label=False,widget=forms.PasswordInput(attrs={'placeholder':'Mot de passe'}))


