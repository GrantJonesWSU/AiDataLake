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
from frontend.models import TrainingCorpus
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
        temperature=0.6,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n\n"]
    )

    return response.choices[0].text

def createDatabaseSchemaString(dbName):
    
    # beginning of schema string
    schemaString = "Instruction: The currently selected database contains the following tables with corresponding rows:"

    # get all entities that match the database name
    entitySet = UserDatabaseEntity.objects.filter(dbName=dbName)

    maxGroupingKey = 0

    # Count to the highest grouping key which is the number of tables minus 1.
    for entity in entitySet:
        if entity.localGroupingKey > maxGroupingKey:
            maxGroupingKey = entity.localGroupingKey
    
    # loop through tables by group key
    for currentGroupKey in range(maxGroupingKey + 1):
        # loop through all entities to look for table by current group key
        for entity in entitySet:
            if entity.localGroupingKey == currentGroupKey and entity.tableColumn == 0:

                # add a table entry to the schema string
                schemaString += "\ntable " + entity.elementName + " with columns "
                

                columnsCount = 0

                # loop through all entities to look for columns that belong to current table
                for entity2 in entitySet:
                    if entity2.localGroupingKey == currentGroupKey and entity2.tableColumn == 1:
                        # add to the column count
                        columnsCount += 1
                
                # if only one column in table, trim the 's' off columns and then add the single column name.
                if columnsCount == 1:
                    for entity2 in entitySet:
                        schemaString += entity2.elementName + "; "

                # loop through columns in table and add to schema string, add and before the last item
                else:
                    for entity2 in entitySet:
                        if entity2.localGroupingKey == currentGroupKey and entity2.tableColumn == 1:
                            if columnsCount == 1:
                                schemaString += "and " + entity2.elementName + "; "
                            else:
                                schemaString += entity2.elementName + ", "

    # trim last semicolon and add period
    schemaString = schemaString[:-2]
    schemaString += "."

    return schemaString


def TrainGptInputGeneric(input, DbId):    
    # get the database object by id from parameters
    database = UserDatabase.objects.get(id=DbId)
    
    # add currently used database schema string to input and return
    trainedInput = database.schemaString + "\nInput: " + input + "\nOutput:"

    return trainedInput

# prepends the DB schema to the input and adds extra instructions for an SQL query return
def TrainGptInputSql(input, DbId):
    # get the database object by id from parameters
    database = UserDatabase.objects.get(id=DbId)

    # add currently used database schema string and SQL extra instructions to input and return
    trainedInput = database.schemaString + "\nRespond with a syntactically correct MySQL statement based on the given input. Be creative, but the SQL must be correct. Only use the tables and columns given previously.\nInput: " + input + "\nOutput:"

    return trainedInput

# prepends the corpus to the DB trained input
def TrainGptCorpus(input):
    trainedInput = ""
    corpus = TrainingCorpus.objects.all()

    # need to add corpus schema here before the inputs and outputs
    with open("frontend/corpusSchemaTogether.txt") as corpusSchema:
        corpusSchemaText = corpusSchema.read()
        trainedInput += str(corpusSchemaText)

    # add input and output for each entity in the training corpus
    for entity in corpus:
        trainedInput += "\nInput: " + entity.inputText + "\nOutput: " + entity.outputText + "\n"

    trainedInput += "\n"

    return trainedInput + input