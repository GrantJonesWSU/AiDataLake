from django.contrib import admin
from django.urls import path, include
from django.http import request
from django.shortcuts import render
from django.db.models import Q
from django.db import models

from frontend import views

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

