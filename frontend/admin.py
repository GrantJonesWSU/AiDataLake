from django.contrib import admin
from .models import RequestTable
from .models import UserLogin
from .models import UserTable


# Register your models here.
admin.site.register(RequestTable)
admin.site.register(UserLogin)
admin.site.register(UserTable)
