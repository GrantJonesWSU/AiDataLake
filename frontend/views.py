#--------------------------------------------------------
#Imports
#--------------------------------------------------------
import re
from django.http import request
from django.shortcuts import render
from django.utils.timezone import datetime
from django.utils.translation import ugettext
from frontend.models import GptInputOutput
from frontend.models import GptIOManager
from frontend.models import UserLogin
from frontend.models import UserDatabase
from frontend.models import UserDatabaseManager
from frontend.models import UserDatabaseEntity
from frontend.models import UserDatabaseEntityManager
from frontend.gpt3 import GetGptResponse
from frontend.gpt3 import TrainGptInputGeneric
from frontend.gpt3 import TrainGptInputSql
#--------------------------------------------------------

#--------------------------------------------------------
#Function Definitions/Queries
#--------------------------------------------------------
#Assumes no system issues
sysMessage="  "


#Query for active user
activeUser=UserLogin.objects.filter(loginStatus=1)
if(len(activeUser)!=0):
	activeUsername=str(activeUser[1].username)
	activeUserID=int(activeUser[1].id)
else:
	activeUsername="Guest User"
	activeUserID=-1


#Database Dropdown Menu
userDbArr=[]

#Test For Dropdown
dbDropDown=UserDatabaseEntity.objects.all()

#Dropdown Actual Query
#dbDropDown=UserDatabaseEntity.objects.filter(userId=activeUserID)
#if(len(dbDropDown)!=0):
for i in range (len(dbDropDown)):
	dbNameTmp=str(dbDropDown[i].dbName)
	
	if ((dbNameTmp in userDbArr)==False):
		userDbArr.append(dbNameTmp)


#--------------------------------------------------------

#--------------------------------------------------------
# Create your views here
#--------------------------------------------------------

#Home View
def home_view(request):
	return render(request,"home.html",{"logged_in" : activeUsername, "sys_message" : sysMessage,"db_drop_down" : userDbArr})

#Instruction Page View
def instruction_view(request):
	return render(request,"instructions.html")

# Handles User Login
def user_login(request):
	# needs to render the login page and then upon login
	# redirect to the home page
	return render(request, "home.html",{"logged_in" : activeUsername, "sys_message" : sysMessage,"db_drop_down" : userDbArr})

#DB Schema File Is Handled In TestAI.py

# Handles User History Query
def user_history(request):
	#test block
	userHistory = GptInputOutput.objects.all()
	return render(request,"output.html", {"logged_in" : activeUsername,"user_history_list" : userHistory, "sys_message" : sysMessage,"db_drop_down" : userDbArr})

	'''
	#actual execution
	if(activeUserID!=-1):	
		userHistory = GptInputOutput.objects.filter(userId=activeUserID)
		sysMessage = "Successful User History Query"
		return render(request,"output.html", {"logged_in" : activeUsername,"user_history_list" : userHistory, "sys_message" : sysMessage,"db_drop_down" : userDbArr})
	else:
		userHistory = 0
		sysMessage = "Error: User History Query Failed Due To Guest User Status"
		return render(request,"output.html", {"logged_in" : activeUsername,"user_history_list" : userHistory, "sys_message" : sysMessage,"db_drop_down" : userDbArr})
	'''
	

# Handles Recent Meta Query
def recent_meta(request):
	#test block
	recentMeta = GptInputOutput.objects.all()
	return render(request,"output.html", {"logged_in" : activeUsername,"user_history_list" : userHistory, "sys_message" : sysMessage,"db_drop_down" : userDbArr})

	'''
	#actual execution
	#EDIT TO FIT RECENT META FUNCTIONALITY
	if(activeUserID!=-1):	
		userHistory = GptInputOutput.objects.filter(userId=activeUserID)
		sysMessage = "Successful Recent Meta Query"
		return render(request,"output.html", {"logged_in" : activeUsername,"user_history_list" : userHistory, "sys_message" : sysMessage,"db_drop_down" : userDbArr})
	else:
		recentMeta = 0
		sysMessage = "Error: Recent Meta Query Failed Due To Guest User Status"
		return render(request,"output.html", {"logged_in" : activeUsername,"user_history_list" : userHistory, "sys_message" : sysMessage,"db_drop_down" : userDbArr})
	'''
  
#GPT View
def gpt_view(request):
	gptOutput = "none, may have been an error or bug"

	if request.method == "POST":
		# Create Dict of Request
		readRequest=request.POST

		# Store Query String
		queryString=readRequest["genericGptInput"]

		# Need to change the hardcoded 1 to a stored db name for the user to select
		trainedInput = TrainGptInputGeneric(queryString, 1)
		gptOutput = "OUTPUT: " + GetGptResponse(trainedInput)

		gptObject = GptInputOutput.objects.createGptIO(queryString, trainedInput, gptOutput, datetime.now())
		gptObject.save()

	return render(request,"output.html", {"logged_in" : activeUsername, "gpt_output" : gptOutput, "sys_message" : sysMessage,"db_drop_down" : userDbArr})

#GPT3 SQL View
def gpt_sql_view(request):
	gptOutput = "none, may have been an error or bug"

	if request.method == "POST":
		# Create Dict of Request
		readRequest=request.POST

		# Store Query String
		queryString=readRequest["sqlGptInput"]

		# Need to change the hardcoded 1 to a stored db name for the user to select
		trainedInput = TrainGptInputGeneric(queryString, 1)
		gptOutput = "OUTPUT: SELECT " + str(GetGptResponse(trainedInput))

		# Save to Database
		gptObject = GptInputOutput.objects.createGptIO(queryString, trainedInput, gptOutput, datetime.now())
		gptObject.save()
	
	return render(request,"output.html", {"logged_in" : activeUsername,"gpt_output" : gptOutput, "sys_message" : sysMessage,"db_drop_down" : userDbArr})
