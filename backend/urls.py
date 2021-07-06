"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')

Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from frontend import views
from frontend import urls
from frontend import testAI
from frontend import gpt3

urlpatterns = [
    path('',views.home_view, name='home'),
    path('instructions',views.instruction_view,name='readMe'),
    path('userLogin',urls.user_login,name='userLogin'),
    path('fileUpload',testAI.file_upload,name='dbfile'),
    path('userHistory',urls.user_history,name='userhist'),
    path('recentMeta',urls.recent_meta,name='recentMeta'),
    path('GPT3',gpt3.gpt_function,name='gpt3'),
    path('GPT3Location',gpt3.gpt_location_function,name='gpt3Location'),
    path("register", views.register_request, name="register"),
    path('admin/', admin.site.urls),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout")
]
