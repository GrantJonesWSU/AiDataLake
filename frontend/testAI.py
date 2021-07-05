#----------------------------------------------------
# Import Library/Function Definitions
#----------------------------------------------------
#Imports
from django.shortcuts import render
from django.http import HttpRequest
from rest_framework.request import Request
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings


#Functions
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""
#----------------------------------------------------

#----------------------------------------------------
# Variable Declarations
#----------------------------------------------------
tableList=[]
tableCountComp=[]
tableColumn=[]
arrTemp=[]
sqlCommands=[]
#----------------------------------------------------

#---------------------------------------------------
#Enter POST request from prompt
#---------------------------------------------------
def file_upload(request):
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

			return render(request,"home.html")

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

			for i in range(len(tableColumn)):
				groupingKey=i

				for j in range(len(tableColumn[i])):
					if(j==0):
						elementName=tableColumn[i][j]
						dataTypeTemp="N/A"
						tableColumnCheck=0

						#Test Block For Display
						'''
						print("Element Name: ", elementName)
						print("DataType: ",dataTypeTemp)
						print("Table/Column: ",tableColumnCheck)
						print("Grouping Key: ",groupingKey)
						print("-------------------")
						'''

					elif(j%2!=0):
						elementName=tableColumn[i][j]
						dataTypeTemp=tableColumn[i][j+1]
						tableColumnCheck=1

						#Test Block For Display
						'''
						print("Element Name: ", elementName)
						print("DataType: ",dataTypeTemp)
						print("Table/Column: ",tableColumnCheck)
						print("Grouping Key: ",groupingKey)
						print("-------------------")
						'''
						

			#Returns HTML Default View, Edit to route to views instead								
			return render(request,"home.html")