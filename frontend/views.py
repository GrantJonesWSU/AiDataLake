import re
from django.http import request
from django.shortcuts import render
from django.utils.timezone import datetime
from frontend.models import GptInputOutput
from frontend.models import GptIOManager
from frontend.models import UserDatabase
from frontend.models import UserDatabaseManager
from frontend.models import UserDatabaseEntity
from frontend.models import UserDatabaseEntityManager
from frontend.gpt3 import GetGptResponse
from frontend.gpt3 import TrainGptInputGeneric
from frontend.gpt3 import TrainGptInputSql


# Create your views here.
def home_view(request):
	return render(request,"home.html")

def instruction_view(request):
	return render(request,"instructions.html")

# Handles User Login
def user_login(request):
	# needs to render the login page and then upon login
	# redirect to the home page
	return render(request, "home.html")

# Handles DB Schema File
def file_upload(request):
	return render(request,"home.html")

# Handles User History Query
def user_history(request):
	userHistory = GptInputOutput.objects.all()
	# fetch the history and then send to page render

	return render(request,"home.html", {"user_history_list" : userHistory})

# Handles Recent Meta Query
def recent_meta(request):
	recentMeta = "no recent meta to show or encountered error"

	return render(request,"home.html", {"recent_meta_output" : recentMeta})

def gpt_view(request):
	gptOutput = "none, may have been an error or bug"

	if request.method == "POST":
		# Create Dict of Request
		readRequest=request.POST

		# Store Query String
		queryString=readRequest["genericGptInput"]

		trainedInput = TrainGptInputGeneric(queryString, 1)
		gptOutput = GetGptResponse(trainedInput)

		gptObject = GptInputOutput.objects.createGptIO(queryString, trainedInput, gptOutput, datetime.now())
		gptObject.save()

	return render(request,"home.html", {"gpt_output" : gptOutput})
	
def gpt_sql_view(request):
	gptOutput = "none, may have been an error or bug"

	if request.method == "POST":
		# Create Dict of Request
		readRequest=request.POST

		# Store Query String
		queryString=readRequest["sqlGptInput"]

		trainedInput = TrainGptInputSql(queryString, 1, SQLVersion)
		gptOutput = str(GetGptResponse(trainedInput))

		# Save to Database
		gptObject = GptInputOutput.objects.createGptIO(queryString, trainedInput, gptOutput, datetime.now())
		gptObject.save()
	
	return render(request,"home.html", {"gpt_output" : gptOutput})
