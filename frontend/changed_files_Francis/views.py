import re
from django.http import request
from django.shortcuts import render
from django.utils.timezone import datetime
from frontend.models import GptInputOutput
from frontend.models import UserDatabase
from frontend.models import UserDatabaseEntity
from frontend.gpt3 import GetGptResponse
from frontend.gpt3 import TrainGptInputGeneric
from frontend.gpt3 import TrainGptInputSql
 

# Create your views here.
def home_view(request):
	return render(request,"home.html")

def instruction_view(request):
	return render(request,"instructions.html")

#Handles User Login
def user_login(request):
	# needs to render the login page and then upon login
	# redirect to the home page
	return render(request, "home.html")

#Handles DB Schema File
def file_upload(request):
	return render(request,"home.html")

#Handles User History Query
def user_history(request):
	userHistory = "no history to show, or encountered error"
	# could change to a list and then use a loop in the html output area

	# fetch the user's history and then save to the userHistory variable here

	return render(request,"home.html", {"user_history_output" : userHistory})

#Handles Recent Meta Query
def recent_meta(request):
	recentMeta = "no recent meta to show or encountered error"
	# could change to a list and then use a loop in the html output area

	# fetch the recent meta and then save to recentMeta variable here

	return render(request,"home.html", {"recent_meta_output" : recentMeta})

def gpt_view(request):
	gptOutput = "none, may have been an error or bug"

	if request.method == "POST":
		#Create Dict of Request
		readRequest=request.POST

		#Store Query String
		queryString=readRequest["genericGptInput"]

		trainedInput = TrainGptInputGeneric(queryString)
		gptOutput = GetGptResponse(trainedInput)

		# still need to save to DB

	return render(request,"home.html", {"gpt_output" : gptOutput})
	
def gpt_sql_view(request):
	gptOutput = "none, may have been an error or bug"

	if request.method == "POST":
		#Create Dict of Request
		readRequest=request.POST

		#Store Query String
		queryString=readRequest["sqlGptInput"]

		trainedInput = TrainGptInputGeneric(queryString)
		gptOutput = GetGptResponse(trainedInput)

		# still need to save to DB
	
	return render(request,"home.html", {"gpt_output" : gptOutput})
