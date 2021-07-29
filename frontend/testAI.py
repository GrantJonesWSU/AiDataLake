#----------------------------------------------------
# Import Library/Function Definitions
#----------------------------------------------------
from django.shortcuts import render
from django.http import HttpRequest
from django.core.files.storage import default_storage
from django.conf import settings
from django.contrib.auth import get_user_model
from .models import *
from django.db import models
from frontend.gpt3 import createDatabaseSchemaString
from django.utils.timezone import datetime
from frontend.models import UserLogin
#---------------------------------------------------
#Enter POST request from prompt
#---------------------------------------------------
def file_upload(request):
	#----------------------------------------------------
	#Functions
	#----------------------------------------------------
	#find between function
	def find_between( s, first, last ):
		try:
			start = s.index( first ) + len( first )
			end = s.index( last, start )
			return s[start:end]
		except ValueError:
			return ""

	#active user function
	activeUser=UserLogin.objects.filter(loginStatus=1)
	if(len(activeUser)!=0):
		activeUsername=str(activeUser[1].username)
		activeUserID=int(activeUser[1].id)
	else:
		activeUsername="Guest User"
		activeUserID=-1

	sysMessage="Successfully Obtained DB Schema"

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
	#----------------------------------------------------


	#----------------------------------------------------
	# Variable Declarations
	#----------------------------------------------------
	tableList=[]
	tableCountComp=[]
	tableColumn=[]
	arrTemp=[]
	sqlCommands=[]
	#-----------------------------------------------

	if request.method == "POST":
		#Contain db file in local memory
		#Also manipulate as string for file type checking

		readDB=request.FILES
		fileName=str(readDB["myFile"])
		
		#File Type Checking
		if(fileName.find(".sql")==-1):

			#File Type Fail
			print("------------------------------")
			print("Improper file type uploaded, being ignored by functionality")
			print("------------------------------")
			
			sysMessage="ERROR: Improper file type submitted, ignored by application. Please upload a .SQL file"

			return render(request,"home.html",{"logged_in" : activeUsername,"sys_message" : sysMessage,"db_drop_down" : userDbArr})

		else:

			#File Type Success
			print("------------------------------")
			print("Successfully Obtained DB File")
			print("------------------------------")
			
			
			#----------------------------------------------------
			#Read SQL file for schema
			#----------------------------------------------------
		
			data = request.FILES["myFile"] 
			sqlFile=data.read()
			
			
			#Delimits file to SQL commands
			sqlCommands = str(sqlFile).split(';')
			sqlSize=len(sqlCommands)
			#----------------------------------------------------


			#----------------------------------------------------
			#Checks for tables and delimits by finding indicies
			#----------------------------------------------------
			for i in range(sqlSize):
				x=sqlCommands[i].find("CREATE")

				if(x != -1):
					tableList.append(i)

			#Amount of tables stored
			tableCount=len(tableList)
			#----------------------------------------------------


			#----------------------------------------------------
			#Checks blocks containing table data
			#----------------------------------------------------
			for i in range(tableCount):

				tmp=tableList[i]
				y=sqlCommands[tmp].find("TABLE")

				if (y != -1):
					tableCountComp.append(1)
				else:
					tableCountComp.append(0)

			#----------------------------------------------------


			#Table Column Format at any particular location 
			#Contains array w/ 0 being table name, odd being column name, even being data type of previous column name
			#----------------------------------------------------
			#Table name and column name extracted and formatted
			#----------------------------------------------------
			for i in range(len(tableList)):
				if(tableCountComp[i]!=0):
					tmp=tableList[i]
					tableName= find_between( sqlCommands[tmp] , "TABLE" , "(" )
					arrTemp.append(tableName)
					
					columnNames= find_between( sqlCommands[tmp] , "(" , ") ENGINE" )
					columnNameSplit=columnNames.split(",")
					
				
					for i in range(len(columnNameSplit)):
						j=columnNameSplit[i].split("NOT NULL")

						#!!!May need to be modified to accomodate formatting
						#--------------------
						k=j[0].split(" ",3)
						arrTemp.append(k[2])
						arrTemp.append(k[3])
						#----------------------
					
					tableColumn.append(arrTemp)
				else:
					tmp=tableList[i]
					dataBaseName= find_between( sqlCommands[tmp] , "EXISTS" ,"DEFAULT")
					print(dataBaseName)

				arrTemp=[]
			#----------------------------------------------------


			#----------------------------------------------------
			#Format For Writing To DB
			#----------------------------------------------------
			print(tableColumn)
			for i in range(len(tableColumn)):
				groupingKey=i

				for j in range(len(tableColumn[i])):

					

					if(j==0):
						elementNameTemp=tableColumn[i][j]
						dataTypeTemp="N/A"
						tableColumnCheck=0

						#Test Block For Display
						'''
						print("Element Name: ", elementNameTemp)
						print("DataType: ",dataTypeTemp)
						print("Table/Column: ",tableColumnCheck)
						print("Grouping Key: ",groupingKey)
						print("-------------------")
						'''

					else:	
						if(j%2!=0):
							elementNameTemp=tableColumn[i][j]
							dataTypeTemp=str(tableColumn[i][j+1])
							tableColumnCheck=1

							#Test Block For Display
							'''
							print("Element Name: ", elementNameTemp)
							print("DataType: ",dataTypeTemp)
							print("Table/Column: ",tableColumnCheck)
							print("Grouping Key: ",groupingKey)
							print("-------------------")
							'''
							
					if(j==0 or j%2!=0):	
						row = UserDatabaseEntity(
							dbName=fileName,
							userId=activeUserID,
							elementName=elementNameTemp,
							dataType=dataTypeTemp,
							tableColumn=tableColumnCheck,
							localGroupingKey=groupingKey)
						row.save()

					
					

					
	
		db = UserDatabase(
			dbName=fileName,
			schemaString=createDatabaseSchemaString(fileName),
			dateTimeCreated=datetime.now()
		)
		db.save()

		print("DONE WRITING USER DB TO SYSTEM DB")
		#Returns HTML Default View, Edit to route to views instead								
		return render(request,"home.html",{"logged_in" : activeUsername,"sys_message" : sysMessage,"db_drop_down" : userDbArr})
