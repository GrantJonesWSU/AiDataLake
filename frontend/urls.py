from django.urls import path
from frontend import views
from frontend.models import GptIO

gpt_response_view = views.GptResponseView.as_view(
    queryset=GptIO.objects.order_by("-log_date")[:1], # :1 limits the results to the one most recent
    context_object_name="gpt_response",
    template_name = "frontend/gpt_response.html",
)

urlpatterns = [
    path('', views.home_view, name='home'),
    path('gpt_response', gpt_response_view, name='gpt_response')
]
