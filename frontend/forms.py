from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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

# django.core.exceptions.ImproperlyConfigured
# Creating a ModelForm without either the 'fields' attribute
# or the 'exclude' attribute is prohibited; form UserDatabaseForm needs updating.
# class UserDatabaseForm(forms.ModelForm):
#     class Meta:
#         model = UserDatabase

# django.core.exceptions.FieldError: Unknown field(s) (userInput, gptOutput) specified for UserDatabaseEntity
# class UserDatabaseEntityForm(forms.ModelForm):
#     class Meta:
#         model = UserDatabaseEntity
#         fields = ("userInput", "gptOutput")
       

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
