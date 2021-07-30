from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from frontend import views
from frontend import testAI
from frontend import gpt3

urlpatterns = [
    path('', views.home_view, name='home'),
    path('instructions', views.instruction_view, name='readMe'),
    # path('userLogin', views.user_login, name='userLogin'),
    path('fileUpload', testAI.file_upload, name='dbfile'),
    path('userHistory', views.user_history, name='userhist'),
    path('GPT3', views.gpt_view, name='gpt3'),
    path('GPT3Sql', views.gpt_sql_view, name='gpt3sql'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='pass_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="pass_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='pass_reset_complete.html'), name='password_reset_complete'),
    path("password_reset_form", views.password_reset_request, name="password_reset"),
]
