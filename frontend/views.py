import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from frontend.models import GptIO
from frontend.forms import GptIOForm
from frontend.gptProcessing import GetGptResponse
from django.views.generic import ListView

# Create your views here.

class GptResponseView(ListView):
    model = GptIO

    def get_context_data(self, **kwargs):
        context = super(GptResponseView, self).get_context_data(**kwargs)
        return context

def home_view(request):
    form = GptIOForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.output_text = GetGptResponse(message.input_text)
            message.log_date = datetime.now()
            message.save()
            return redirect("gpt_response")
    else:
        return render(request, "frontend/home.html", {"form": form})