from django.http import request
from django.shortcuts import render
import re
from django.utils.timezone import datetime

 

# Create your views here.
def home_view(request):
	return render(request,"home.html")

def instruction_view(request):
	return render(request,"instructions.html")

#Handles User Login
def user_login(request):
	return render(request,"home.html")

#Handles DB Schema File
def file_upload(request):
	return render(request,"home.html")

#Handles User History Query
def user_history(request):
	return render(request,"home.html")

#Handles Recent Meta Query
def recent_meta(request):
	return render(request,"home.html")

