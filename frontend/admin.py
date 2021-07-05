from django.contrib import admin
from models import UserLogin
from models import GptInputOutput
from models import UserDatabase
from models import UserDatabaseEntity


# Register your models here.
admin.site.register(UserLogin)
admin.site.register(GptInputOutput)
admin.site.register(UserDatabase)
admin.site.register(UserDatabaseEntity)