from django.contrib import admin
from django.urls import path
from frontend import views
from frontend import testAI
from frontend import gpt3
from frontend import decorators

urlpatterns = [
    path('', views.home_view, name='home'),
    path('instructions', views.instruction_view, name='readMe'),
    path('userLogin', views.user_login, name='userLogin'),
    path('fileUpload', testAI.file_upload, name='dbfile'),
    path('userHistory', views.user_history, name='userhist'),
    path('recentMeta', views.recent_meta, name='recentMeta'),
    path('GPT3', views.gpt_view, name='gpt3'),
    path('GPT3Sql', views.gpt_sql_view, name='gpt3sql'),
    path('loginNeeded', decorators.non_user, name='NAU'),
]
