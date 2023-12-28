from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

class RegisterTestCase(APITestCase):
    def test_register_user(self):
        data = {
                'username':'user01', 
                'email':'user01@gmail.com', 
                'password':'user01@123',
                'password2':'user01@123'
                }
        
        response = self.client.post(reverse('register'), data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        
        
class LoginLogoutTestcase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user01', password='user01@123')
        
    def test_login(self):
        data = {'username':'user01', 'password':'user01@123'}
        response = self.client.post(reverse('login'), data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        
    def test_logout(self):
        token = Token.objects.get(user__username='user01')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post(reverse('logout'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)