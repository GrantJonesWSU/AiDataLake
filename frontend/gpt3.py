#----------------------------------------------------
# Import Library/Function Definitions
#----------------------------------------------------
#Imports
from django.shortcuts import render
from django.http import HttpRequest
from rest_framework.request import Request
#----------------------------------------------------

#Handles GPT3 Operation
def gpt_function(request):
	if request.method == "POST":
		#Create Dict of Request
		readRequest=request.POST

		#Store Query String
		queryString=readRequest["search"]
	
	return render(request,"home.html")

def gpt_location_function(request):
	if request.method == "POST":
		#Create Dict of Request
		readRequest=request.POST

		#Store Query String
		queryString=readRequest["searchLocation"]
	return render(request,"home.html")
	