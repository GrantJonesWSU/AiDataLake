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

def get_userdbs(UserLogin):

	try:
		# Find all dbs in UserDatabase with the user ID, most recent one should appear first.
		queryset = UserDatabase.objects.filter(userId_id=UserLogin).order_by("-dateTimeCreated")
		# print([db.dbName for db in queryset])
		return [db.dbName for db in queryset]
	except UserDatabase.DoesNotExist:
		print(UserDatabase.DoesNotExist)
		pass
	return []

# Create your views here.
def home_view(request):
	# rubel: feeds database list to template, needs to be copied to other views
	UserLogin = 1 # replace with request formdata from authentication?????
	userdbs = get_userdbs(UserLogin)
	return render(request,"home.html", {"user_databases": userdbs})

def instruction_view(request):
	return render(request,"instructions.html")

# Handles User Login
def user_login(request):
	# needs to render the login page and then upon login
	# redirect to the home page
	UserLogin = 1 # replace with request formdata from authentication?
	userdbs = get_userdbs(UserLogin)
	return render(request,"home.html", {"user_databases": userdbs})

# Handles DB Schema File
def file_upload(request):
	UserLogin = 1 # replace with request formdata from authentication?????
	userdbs = get_userdbs(UserLogin)
	return render(request,"home.html", {"user_databases": userdbs})

# Handles User History Query
def user_history(request):
	userHistory = GptInputOutput.objects.all()
	# fetch the history and then send to page render
	UserLogin = 1 # replace with request formdata from authentication?????
	userdbs = get_userdbs(UserLogin)
	return render(request,"home.html", {"user_history_list" : userHistory, "user_databases": userdbs})

# Handles Recent Meta Query
def recent_meta(request):
	recentMeta = "no recent meta to show or encountered error"
	UserLogin = 1 # replace with request formdata from authentication?????
	userdbs = get_userdbs(UserLogin)
	return render(request,"home.html", {"recent_meta_output" : recentMeta, "user_databases": userdbs})

def gpt_view(request):
	gptOutput = "none, may have been an error or bug"

	if request.method == "POST":
		# Create Dict of Request
		readRequest=request.POST

		# Store Query String
		queryString=readRequest["genericGptInput"]

		# Need to change the hardcoded 1 to a stored db name for the user to select
		trainedInput = TrainGptInputGeneric(queryString, 1)
		gptOutput = "OUTPUT: " + str(GetGptResponse(trainedInput))

		gptObject = GptInputOutput.objects.createGptIO(queryString, trainedInput, gptOutput, datetime.now())
		gptObject.save()
	UserLogin = 1 # replace with request formdata from authentication?????
	userdbs = get_userdbs(UserLogin)
	return render(request,"home.html", {"gpt_output" : gptOutput, "user_databases": userdbs})
	
def gpt_sql_view(request):
	gptOutput = "none, may have been an error or bug"

	if request.method == "POST":
		# Create Dict of Request
		readRequest=request.POST

		# Store Query String
		queryString=readRequest["sqlGptInput"]
		SQLVersion = readRequest["SQLFlavor"]

		# Need to change the hardcoded 1 to a stored db name for the user to select
		trainedInput = TrainGptInputSql(queryString, 1, SQLVersion)
		print(trainedInput)
		gptOutput = str(GetGptResponse(trainedInput))

		# Save to Database
		gptObject = GptInputOutput.objects.createGptIO(queryString, trainedInput, gptOutput, datetime.now())
		gptObject.save()
	UserLogin = 1 # replace with request formdata from authentication?????
	userdbs = get_userdbs(UserLogin)
	return render(request,"home.html", {"gpt_output" : gptOutput, "user_databases": userdbs})	
