# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

#Removed django & security related model information from the schema

class UserLogin(models.Model):
    userName = models.TextField()
    password = models.TextField()
    dateAccountCreated = models.DateField(db_column='dateAccountCreated')  # Field name made lowercase.
    loginStatus = models.IntegerField(db_column='loginStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'UserLogin'

class GptIOManager(models.Manager):
    def createGptIO(self, userInput, trainedInput, gptOutput, requestDateTime):
        gptIO = self.create(userInput=userInput, trainedInput=trainedInput, gptOutput=gptOutput, requestDateTime=requestDateTime)
        return gptIO

class GptInputOutput(models.Model):
    userInput = models.TextField(db_column='userInput')  # Field name made lowercase.
    trainedInput = models.TextField(db_column='fullRequestInput')  # Field name made lowercase.
    gptOutput = models.TextField(db_column='gptOutput')  # Field name made lowercase.
    requestDateTime = models.DateTimeField(db_column='requestDateTime')  # Field name made lowercase.
    
    objects = GptIOManager()

    class Meta:
        db_table = 'GptInputOutput'

class UserDatabaseManager(models.Manager):
    def createGptIO(self, dbName, userId, schemaString, dateTimeCreated):
        userDb = self.create(dbName=dbName, userId=userId, schemaString=schemaString, dateTimeCreated=dateTimeCreated)
        return userDb

class UserDatabase(models.Model):
    dbName = models.CharField(max_length=50)
    userId = models.ForeignKey("UserLogin", on_delete=models.CASCADE, null=True)
    schemaString = models.TextField(db_column='schemaString')
    dateTimeCreated = models.DateTimeField(db_column='dateTimeCreated')

    objects = UserDatabaseManager()
    class Meta:
        db_table = 'UserDatabase'

class UserDatabaseEntityManager(models.Manager):
    def createGptIO(self, databaseId, userId, tableOrColumn, dataType, localGroupingKey, description):
        userDbEntity = self.create(databaseId=databaseId, userId=userId, tableOrColumn=tableOrColumn, dataType=dataType, localGroupingKey=localGroupingKey, description=description)
        return userDbEntity

class UserDatabaseEntity(models.Model):
    dbName = models.TextField("dbName")
    userId = models.ForeignKey("UserLogin", on_delete=models.CASCADE, null=True)
    tableColumn = models.IntegerField()
    dataType = models.TextField(db_column='dataType')
    localGroupingKey = models.IntegerField(db_column='localGroupingKey')
    elementName = models.CharField(max_length=50)

    objects = UserDatabaseEntityManager()

    class Meta:
        db_table = 'UserDatabaseEntity'

class TrainingCorpus(models.Model):
    schemaText = models.TextField()
    inputText = models.TextField()
    outputText = models.TextField()

    class Meta:
        db_table = 'TrainingCorpus'