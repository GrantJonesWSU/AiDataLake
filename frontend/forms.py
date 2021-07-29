from django import forms
<<<<<<< HEAD
=======
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
>>>>>>> Frank-dev
from frontend.models import UserLogin
from frontend.models import GptInputOutput
from frontend.models import UserDatabase
from frontend.models import UserDatabaseEntity

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = UserLogin
<<<<<<< HEAD
        fields = ("username", "password",)
=======
        fields = ("userName", "password",)
>>>>>>> Frank-dev

class GptInputOutputForm(forms.ModelForm):
    class Meta:
        model = GptInputOutput
<<<<<<< HEAD
        fields = ("userInput", "sqlGeneration")

class UserDatabaseForm(forms.ModelForm):
    class Meta:
        model = UserDatabase

class UserDatabaseEntityForm(forms.ModelForm):
    class Meta:
        model = UserDatabaseEntity
=======
        fields = ("userInput", "gptOutput")
       

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def clean_email(self):
		email = self.cleaned_data.get("email")
		count = User.objects.filter(email=email).count()
		if count > 0:
			raise forms.ValidationError("email already in use.")
		return email

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
>>>>>>> Frank-dev
