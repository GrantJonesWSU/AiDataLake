
import re
from django.http import request
from django.shortcuts import render, redirect
from django.utils.timezone import datetime
from frontend.models import GptInputOutput
from frontend.models import GptIOManager
from frontend.models import UserDatabase
from frontend.models import UserLogin
from frontend.models import UserDatabaseManager
from frontend.models import UserDatabaseEntity
from frontend.models import UserDatabaseEntityManager
from frontend.gpt3 import GetGptResponse
from frontend.gpt3 import TrainGptInputGeneric
from frontend.gpt3 import TrainGptInputSql
from frontend.gpt3 import TrainGptCorpus
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages #import messages
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
#--------------------------------------------------------

#--------------------------------------------------------
#Function Definitions/Queries
#--------------------------------------------------------
#Assumes no system issues
sysMessage="  "


#Query for active user
def get_userinfo(request):
	# This should be fixed to return real user info.
	# Maybe this info can be stored in session at login time?
	# activeUser=UserLogin.objects.filter(loginStatus=1)
	# if(len(activeUser)!=0):
	# 	activeUsername=str(activeUser[1].username)
	# 	activeUserID=int(activeUser[1].id)
	return "Guest User", 1

def get_userdbs(userID):
	# Query based on userID in UserDatabase
	# User dbs could also be saved in session.
	try:
		# Find all dbs in UserDatabase with the user ID, most recent one should appear first.
		queryset = UserDatabase.objects.filter(userId_id=userID).order_by("-dateTimeCreated")
		# print([db.dbName for db in queryset])
		return [db.dbName for db in queryset]
	except UserDatabase.DoesNotExist:
		print(UserDatabase.DoesNotExist)
		pass
	return []

#--------------------------------------------------------

#--------------------------------------------------------
# Create your views here
#--------------------------------------------------------

#Home View
def home_view(request):
	sysMessage = ""
	activeUsername, userID = get_userinfo(request)
	userDbArr = get_userdbs(userID)
	return render(request,"home.html",{"logged_in" : activeUsername, "sys_message" : sysMessage,"db_drop_down" : userDbArr})

#Instruction Page View
def instruction_view(request):
	return render(request,"instructions.html")

#DB Schema File Is Handled In TestAI.py

# Handles User History Query
def user_history(request):
	sysMessage = ""
	activeUsername, userID = get_userinfo(request)
	userDbArr = get_userdbs(userID)
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
	return render(request, "home.html")

# Handles DB Schema File
def file_upload(request):
	return render(request,"home.html")

def gpt_view(request):
	gptOutput = "none, may have been an error or bug"

	if request.method == "POST":
		# Create Dict of Request
		readRequest=request.POST

		# Store Query String
		queryString=readRequest["genericGptInput"]

		# Need to change the hardcoded 1 to a stored db name for the user to select
		trainedInput = TrainGptInputGeneric(queryString, 1)
		gptOutput = "Output: " + GetGptResponse(trainedInput)

		# Create a gpt I/O object and save it 
		gptObject = GptInputOutput.objects.createGptIO(queryString, trainedInput, gptOutput, datetime.now())
		gptObject.save()

	sysMessage = ""
	activeUsername, userID = get_userinfo(request)
	userDbArr = get_userdbs(userID)
	return render(request,"home.html", {"logged_in" : activeUsername, "gpt_output" : gptOutput, "sys_message" : sysMessage,"db_drop_down" : userDbArr})
	
def gpt_sql_view(request):
	gptOutput = "none, may have been an error or bug"

	if request.method == "POST":
		# Create Dict of Request
		readRequest=request.POST

		# Store Query String
		queryString=readRequest["sqlGptInput"]

		# Need to change the hardcoded 1 to a stored db name for the user to select
		trainedInput = TrainGptInputSql(queryString, 1)
		trainedInput = TrainGptCorpus(trainedInput)
		gptOutput = "Output: " + str(GetGptResponse(trainedInput))

		# Save to Database
		gptObject = GptInputOutput.objects.createGptIO(queryString, trainedInput, gptOutput, datetime.now())
		gptObject.save()

	sysMessage = ""
	activeUsername, userID = get_userinfo(request)
	userDbArr = get_userdbs(userID)
	return render(request,"home.html", {"logged_in" : activeUsername,"gpt_output" : gptOutput, "sys_message" : sysMessage,"db_drop_down" : userDbArr})

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			# Some error checks.
			if form.get("username") != form.cleaned_data.get("username"):
				messages.error(request, "Invalid User Name")
			elif form.get("password") != form.cleaned_data.get("password"):
				messages.error(request, "Invalid password")
			else: # Valid registration
				user = form.save()
				login(request, user)
				messages.success(request, "Registration successful." )
				return redirect("/home")
		else:
			messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request, "register.html", {"register_form": form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "pass_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password_reset_form.html", context={"password_reset_form":password_reset_form})
