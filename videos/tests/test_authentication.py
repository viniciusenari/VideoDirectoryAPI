from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Videos-list')
        self.user = User.objects.create_user('Test user', password = '123456')

    def test_user_authentication(self):
        user = authenticate(username='Test user', password='123456')
        self.assertTrue((user is not None) and user.is_authenticated)
    
    def test_user_authentication_incorrect_username(self):
        user = authenticate(username='Test user 2', password='123456')
        self.assertFalse((user is not None) and user.is_authenticated)
    
    def test_user_authentication_incorrect_password(self):
        user = authenticate(username='Test user', password='1234567')
        self.assertFalse((user is not None) and user.is_authenticated)
    
    def test_get_request_authenticated_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)