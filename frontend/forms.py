from django import forms
from frontend.models import UserLogin
from frontend.models import GptInputOutput
from frontend.models import UserDatabase
from frontend.models import UserDatabaseEntity

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = UserLogin
        fields = ("username", "password",)

class GptInputOutputForm(forms.ModelForm):
    class Meta:
        model = GptInputOutput
        fields = ("userInput", "sqlGeneration")

class UserDatabaseForm(forms.ModelForm):
    class Meta:
        model = UserDatabase

class UserDatabaseEntityForm(forms.ModelForm):
    class Meta:
        model = UserDatabaseEntity