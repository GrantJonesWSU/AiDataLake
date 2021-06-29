from django import forms
from frontend.models import GptIO

class GptIOForm(forms.ModelForm):
    class Meta:
        model = GptIO
        fields = ("input_text",)  # Note: the trailing comma is required
