#----------------------------------------------------
# Import Library/Function Definitions
#----------------------------------------------------
#Imports
import os
import openai
from django.shortcuts import render
from django.http import HttpRequest
from rest_framework.request import Request
from frontend.models import UserDatabase
from frontend.models import UserDatabaseEntity
#----------------------------------------------------

#gpt-3 key
openai.api_key = "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"

#----------------------------------------------------
#Handles GPT3 Operation
#----------------------------------------------------
def GetGptResponse(gpt_input):
    response = openai.Completion.create(
        engine="davinci-instruct-beta",
        prompt=gpt_input,
        temperature=0.7,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return response.choices[0].text

def createDatabaseSchemaString(dbName):
    
    schemaString = "INSTRUCTIONS: The currently selected database has "

    entitySet = UserDatabaseEntity.objects.filter(dbName=dbName)

    maxGroupingKey = 0

    for entity in entitySet:
        if entity.localGroupingKey > maxGroupingKey:
            maxGroupingKey = entity.localGroupingKey
    
    for currentGroupKey in range(maxGroupingKey + 1): 
        for entity in entitySet:
            if entity.localGroupingKey == currentGroupKey and entity.tableColumn == 0:
                schemaString += "table " + entity.elementName + " with columns "
                for entity2 in entitySet:
                    if entity2.localGroupingKey == currentGroupKey and entity2.tableColumn == 1:
                        schemaString += entity2.elementName + ", "

    schemaString = schemaString[:-2] # trim last comma
    schemaString += "."

    # loop through entities that match databaseId
    # for every table add "table TABLE_NAME with columns" to the schemaString
    # under each table for each column add " COLUMN_NAME,"
    # and then just "COLUMN_NAME" for the last column
    # can either return the schemaString or save directly to database

    return schemaString


def TrainGptInputGeneric(input, DbId):    
    database = UserDatabase.objects.get(id=DbId)
    
    # add currently used database schema string to input and return
    trainedInput = database.schemaString + "\nINPUT: " + input + "\nOUTPUT: "

    return trainedInput

def TrainGptInputSql(input, DbId):
    database = UserDatabase.objects.get(id=DbId)

    # add currently used database schema string to input and return
    trainedInput = database.schemaString + " Return a syntactically correct MySQL statement based on the given input.\nINPUT: " + input + "\nOUTPUT: "


    return trainedInput