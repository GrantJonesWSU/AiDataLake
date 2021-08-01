from django.http import response
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from frontend.forms import *
from django.contrib.auth.forms import AuthenticationForm

class BaseTest(TestCase):
    def setUp(self):
        self.register_url=reverse('register')
        self.login_url=reverse('login')
        self.account_url=reverse('account')

        
        self.test_user = User.objects.create_user(
            email = "test@gmail.com",
            username = "TestUser", 
            password="jopkoplop",
            )
        
        self.test_user2 = User.objects.create_user(
            email="test2@gmail.com",
            username = "TestUser2", 
            password="jopkoplop",
            )


        return super().setUp()

class RegisterTest(BaseTest):
    def test_correct_page(self):
        response=self.client.get(self.register_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'register.html')

    def test_succesfull_registration(self):
        data={
            'email':'testemail@gmail.com',
            'username':'username',
            'password1':'jopkoplop',
            'password2':'jopkoplop',
            }
        form = NewUserForm(data)
        self.assertTrue(form.is_valid())

    def test_unsuccesfull_registration(self):
        data={
            'email':'',
            'username':'',
            'password1':'',
            'password2':'',
            }
        form = NewUserForm(data)
        self.assertFalse(form.is_valid())

    def test_different_password1(self):
        data={
            'email':'testemail@gmail.com',
            'username':'username',
            'password1':'jopkoploppp',
            'password2':'jopkoplop',
            }
        form = NewUserForm(data)
        self.assertFalse(form.is_valid())

    def test_different_password2(self):
        data={
            'email':'testemail@gmail.com',
            'username':'username',
            'password1':'jopkoplop',
            'password2':'jopkoploppp',
            }
        form = NewUserForm(data)
        self.assertFalse(form.is_valid())
    
    def test_missing_password1(self):
        data={
            'email':'testemail@gmail.com',
            'username':'username',
            'password1':'',
            'password2':'jopkoplop',
            }
        form = NewUserForm(data)
        self.assertFalse(form.is_valid())

    def test_missing_password2(self):
        data={
            'email':'testemail@gmail.com',
            'username':'username',
            'password1':'jopkoplop',
            'password2':'',
            }
        form = NewUserForm(data)
        self.assertFalse(form.is_valid())

    def test_only_password1(self):
        data={
            'email':'',
            'username':'',
            'password1':'jopkoplop',
            'password2':'',
            }
        form = NewUserForm(data)
        self.assertFalse(form.is_valid())
    
    def test_only_password2(self):
        data={
            'email':'',
            'username':'',
            'password1':'',
            'password2':'jopkoplop',
            }
        form = NewUserForm(data)
        self.assertFalse(form.is_valid())
    
    def test_only_both_password(self):
        data={
            'email':'',
            'username':'',
            'password1':'jopkoplop',
            'password2':'jopkoplop',
            }
        form = NewUserForm(data)
        self.assertFalse(form.is_valid())

    def test_missing_both_passwords(self):
        data={
            'email':'testemail@gmail.com',
            'username':'username',
            'password1':'',
            'password2':'',
            }
        form = NewUserForm(data)
        self.assertFalse(form.is_valid())

    def test_similar_password(self):
        data={
            'email':'testemail@gmail.com',
            'username':'username',
            'password1':'username',
            'password2':'username',
            }
        form = NewUserForm(data)
        self.assertFalse(form.is_valid())

    def test_short_password(self):
        data={
            'email':'testemail@gmail.com',
            'username':'username',
            'password1':'jop',
            'password2':'jop',
            }
        form = NewUserForm(data)
        self.assertFalse(form.is_valid())

    def test_common_password(self):
        data={
            'email':'testemail@gmail.com',
            'username':'username',
            'password1':'password',
            'password2':'password',
            }
        form = NewUserForm(data)
        self.assertFalse(form.is_valid())

    def test_numeric_password(self):
        data={
            'email':'testemail@gmail.com',
            'username':'username',
            'password1':'1223334444',
            'password2':'1223334444',
            }
        form = NewUserForm(data)
        self.assertFalse(form.is_valid())

    def test_empty_username(self):
        data={
            'email':'testemail@gmail.com',
            'username':'',
            'password1':'jopkoplop',
            'password2':'jopkoplop',
            }
        form = NewUserForm(data)
        self.assertFalse(form.is_valid())
    
    def test_only_username(self):
        data={
            'email':'',
            'username':'TestUser',
            'password1':'',
            'password2':'',
            }
        form = NewUserForm(data)
        self.assertFalse(form.is_valid())
    
    def test_taken_username(self):
        data={
            'email':'testemail@gmail.com',
            'username':'TestUser',
            'password1':'jopkoplop',
            'password2':'jopkoplop',
            }
        form = NewUserForm(data)
        self.assertFalse(form.is_valid())

    def test_blank_email(self):
        data={
            'email':'',
            'username':'username',
            'password1':'jopkoplop',
            'password2':'jopkoplop',
            }
        form = NewUserForm(data)
        self.assertFalse(form.is_valid())
    
    def test_only_email(self):
        data={
            'email':'testemail@gmail.com',
            'username':'',
            'password1':'',
            'password2':'',
            }
        form = NewUserForm(data)
        self.assertFalse(form.is_valid())

    def test_taken_email(self):
        data={
            'email':'test@gmail.com',
            'username':'username',
            'password1':'jopkoplop',
            'password2':'jopkoplop',
            }
        form = NewUserForm(data)
        self.assertFalse(form.is_valid())

    def test_invalid_email(self):
        data={
            'email' : "test",
            'username':'username',
            'password1':'jopkoplop',
            'password2':'jopkoplop',
            }
        form = NewUserForm(data, instance=self.test_user)
        self.assertFalse(form.is_valid())
    
    def test_invalid_email2(self):
        data={
            'email' : "test2@",
            'username':'username',
            'password1':'jopkoplop',
            'password2':'jopkoplop',
            }
        form = NewUserForm(data)
        self.assertFalse(form.is_valid())
    
    def test_invalid_email3(self):
        data={
            'email' : "test2@gmail",
            'username':'username',
            'password1':'jopkoplop',
            'password2':'jopkoplop',
            }
        form = NewUserForm(data)
        self.assertFalse(form.is_valid())


class LoginTest(BaseTest):
    def test_correct_page(self):
        response=self.client.get(self.login_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'login.html')

    def test_valid_login(self):
        data={
            'username' : "TestUser", 
            'password' : "jopkoplop"
            }
        form = AuthenticationForm(None,data)
        self.assertTrue(form.is_valid())

    def test_invalid_login(self):
        data={
            'username' : "", 
            'password' : ""
            }
        form = AuthenticationForm(None,data)
        self.assertFalse(form.is_valid())

    def test_only_username(self):
        data={
            'username' : "TestUser", 
            'password' : ""
            }
        form = AuthenticationForm(None,data)
        self.assertFalse(form.is_valid())
    
    def test_only_password(self):
        data={
            'username' : "", 
            'password' : "jopkoplop"
            }
        form = AuthenticationForm(None,data)
        self.assertFalse(form.is_valid())
    
    def test_wrong_username(self):
        data={
            'username' : "testuser", 
            'password' : "jopkoplop"
            }
        form = AuthenticationForm(None,data)
        self.assertFalse(form.is_valid())

    def test_wrong_password(self):
        data={
            'username' : "testuser", 
            'password' : "jopk"
            }
        form = AuthenticationForm(None,data)
        self.assertFalse(form.is_valid())


class AccountFormTest(BaseTest):


    def test_correct_page(self):
        self.client.login(username='TestUser', password='jopkoplop')
        response=self.client.get(self.account_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'account.html')

    def test_valid_change_both(self):
        data={
            'username' : "TestUserNew", 
            'email' : "testNew@gmail.com"
            }
        form = AccountUpdateForm(data, instance=self.test_user)
        self.assertTrue(form.is_valid())


    def test_valid_change_username(self):
        data={
            'username' : "TestUserNew2",
            'email' : "test@gmail.com"
            }
        form = AccountUpdateForm(data, instance=self.test_user)
        self.assertTrue(form.is_valid())

    def test_valid_change_email(self):
        data={
            'username':"TestUser",
            'email' : "testNew2@gmail.com"
            }
        form = AccountUpdateForm(data, instance=self.test_user)
        self.assertTrue(form.is_valid())

    def test_invalid_change_blank(self):
        data={
            'username' : ""
            }
        form = AccountUpdateForm(data, instance=self.test_user)
        self.assertFalse(form.is_valid())

    
    def test_invalid_change_existing_user(self):
        data={
            'username' : "TestUser2", 
            'email' : "test2@gmail.com"
            }
        form = AccountUpdateForm(data, instance=self.test_user)
        self.assertFalse(form.is_valid())

    def test_invalid_change_existing_user_username(self):
        data={
            'username' : "TestUser2"
            }
        form = AccountUpdateForm(data, instance=self.test_user)
        self.assertFalse(form.is_valid())

    def test_invalid_change_existing_user_email(self):
        data={
            'email' : "test2@gmail.com"
            }
        form = AccountUpdateForm(data, instance=self.test_user)
        self.assertFalse(form.is_valid())

    def test_invalid_change_invalid_email(self):
        data={
            'email' : "test"
            }
        form = AccountUpdateForm(data, instance=self.test_user)
        self.assertFalse(form.is_valid())
    
    def test_invalid_change_invalid_email2(self):
        data={
            'email' : "test2@"
            }
        form = AccountUpdateForm(data, instance=self.test_user)
        self.assertFalse(form.is_valid())
    
    def test_invalid_change_invalid_email3(self):
        data={
            'email' : "test2@gmail"
            }
        form = AccountUpdateForm(data, instance=self.test_user)
        self.assertFalse(form.is_valid())



