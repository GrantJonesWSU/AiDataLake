#----------------------------------------------------
# Import Library/Function Definitions
#----------------------------------------------------
#Imports
import os
import openai
from django.shortcuts import render
from django.http import HttpRequest
from rest_framework.request import Request
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

def createDatabaseSchemaString(databaseId):
    
    schemaString = "The currently selected database has "

    # loop through entities that match databaseId
    # for every table add "table TABLE_NAME with columns" to the schemaString
    # under each table for each column add " COLUMN_NAME,"
    # and then just "COLUMN_NAME" for the last column
    # can either return the schemaString or save directly to database

    return schemaString


def TrainGptInputGeneric(input):
	output = ""
    
    # add currently used database schema string to input and return

	return output

def TrainGptInputSql(input):
	output = ""

    # add currently used database schema string to input and return

	return output