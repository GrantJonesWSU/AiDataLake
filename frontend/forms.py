from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from frontend.models import UserLogin
from frontend.models import GptInputOutput
from frontend.models import UserDatabase
from frontend.models import UserDatabaseEntity

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = UserLogin
        fields = ("userName", "password",)

class GptInputOutputForm(forms.ModelForm):
    class Meta:
        model = GptInputOutput
        fields = ("userInput", "gptOutput")

# jango.core.exceptions.ImproperlyConfigured
# Creating a ModelForm without either the 'fields' attribute
# or the 'exclude' attribute is prohibited; form UserDatabaseForm needs updating.
# class UserDatabaseForm(forms.ModelForm):
#     class Meta:
#         model = UserDatabase

# jango.core.exceptions.FieldError: Unknown field(s) (userInput, gptOutput) specified for UserDatabaseEntity
# class UserDatabaseEntityForm(forms.ModelForm):
#     class Meta:
#         model = UserDatabaseEntity
#         fields = ("userInput", "gptOutput")
       

# form for user registration
class NewUserForm(UserCreationForm):

	email = forms.EmailField(required=True)

	# custom form
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	# valid email check
	def clean_email(self):
		email = self.cleaned_data.get("email")
		count = User.objects.filter(email=email).count()
		if count > 0:
			raise forms.ValidationError("email already in use.")
		return email

	# saves user 
	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

# form for account update
class AccountUpdateForm(forms.ModelForm):

	# custom form
	class Meta:
		model = User
		fields = ('email', 'username')

	def get(self, queryset=None):
         # loads the profile of the currently logged in user
         return AccountUpdateForm.objects.get(user=self.request.user)

	# valid email check
	def clean_email(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			try:
				user = User.objects.exclude(pk=self.instance.pk).get(email=email)
			except User.DoesNotExist:
				return email
			raise forms.ValidationError('Email "%s" is already in use.' % email)
	
	# valid username check
	def clean_username(self):
		if self.is_valid():
			username = self.cleaned_data['username']
			try:
				user = User.objects.exclude(pk=self.instance.pk).get(username=username)
			except User.DoesNotExist:
				return username
			raise forms.ValidationError('Username "%s" is already in use.' % username)
