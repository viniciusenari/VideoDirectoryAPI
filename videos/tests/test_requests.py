from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.test import APITestCase
from videos.models import Video, Category
from django.urls import reverse
from rest_framework import status

class VideosTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Videos-list')
        self.category = Category.objects.create(title='Test Category', color='#000000')
        self.video = Video.objects.create(title='Test Video', description='Test Description', url='https://www.youtube.com/watch?v=9bZkp7q19f0', category_id=self.category)

        self.user = User.objects.create_user('Test user', password = '123456')
        self.client.force_authenticate(user=self.user)

    def test_get_videos(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_post_video(self):
        data = {
            'title': 'Test Video 2',
            'description': 'Test Description 2',
            'url': 'https://youtu.be/gBdwZeK4igM',
            'category': self.category.id
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Test Video 2')
        self.assertEqual(response.data['description'], 'Test Description 2')
        self.assertEqual(response.data['url'], 'https://youtu.be/gBdwZeK4igM')
        self.assertEqual(response.data['category_id'], self.category.id)
    
    def test_delete_video(self):
        response = self.client.delete(self.list_url + str(self.video.id) + '/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_put_video(self):
        data = {
            'title': 'Test Video 2',
            'description': 'Test Description 2',
            'url': 'https://youtu.be/gBdwZeK4igM',
            'category': self.category.id
        }
        response = self.client.put(self.list_url + str(self.video.id) + '/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Video 2')
        self.assertEqual(response.data['description'], 'Test Description 2')
        self.assertEqual(response.data['url'], 'https://youtu.be/gBdwZeK4igM')
        self.assertEqual(response.data['category_id'], self.category.id)

class CategoryTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Categories-list')
        self.category = Category.objects.create(title='Test Category', color='#000000')

        self.user = User.objects.create_user('Test user', password = '123456')
        self.client.force_authenticate(user=self.user)

    def test_get_categories(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_post_category(self):
        data = {
            'title': 'Test Category 2',
            'color': '#000000'
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Test Category 2')
        self.assertEqual(response.data['color'], '#000000')
    
    def test_delete_category(self):
        response = self.client.delete(self.list_url + str(self.category.id) + '/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_put_category(self):
        data = {
            'title': 'Test Category 2',
            'color': '#000000'
        }
        response = self.client.put(self.list_url + str(self.category.id) + '/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Category 2')
        self.assertEqual(response.data['color'], '#000000')
    