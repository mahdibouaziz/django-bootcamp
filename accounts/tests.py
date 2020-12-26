from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse
from dj_bootcamp.settings import LOGIN_REDIRECT_URL

# Create your tests here.

User=get_user_model()
class UserTestCase(TestCase):

    #we create in this method any sort of database entries
    #The setUp method create everything i need in the data base
    #and then the test_.... methods will test (reference) what was created during that test session
    def setUp(self):
        #Creating a user
        user_a=User(username="cfe",email="cfe@gmail.com")
        user_a.is_staff=True
        user_a.is_superuser=True

        #Creating a class attribute called user_a_pw that contain the password of our user_a
        self.user_a_pw="some_password"

        user_a.set_password(self.user_a_pw)
        user_a.save()

    #the naming convention is important, you need to start your method with test_ 
    def test_user_exists(self):
        user_count=User.objects.all().count()
        self.assertEqual(user_count,1,"There are Problem when creating Users")
    
    #Verifiy the user password that i set in setUp is correct in the Data base
    def test_user_password(self):
        user=User.objects.get(username="cfe")
        self.assertTrue(user.check_password(self.user_a_pw),"The password when creating user is incorrect")

    def test_login_url(self):
        login_url=reverse("login_view")
        data={
            "username":"cfe",
            "password":self.user_a_pw    
        }
        response=self.client.post(login_url, data, follow=True)
        # print(dir(response))
        status_code=response.status_code
        redirect_path = response.request.get("PATH_INFO")
        self.assertEqual(redirect_path,LOGIN_REDIRECT_URL,"Redirect login URL is false")
        