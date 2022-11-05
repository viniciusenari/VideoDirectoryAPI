from django.test import TestCase
from videos.models import Video, Category

class VideoModelTestCase(TestCase):

    def setUp(self):
        self.video = Video(title='Test Video', description='Test Description', url='https://www.youtube.com/watch?v=9bZkp7q19f0')

    def test_video_str(self):
        self.assertEqual(self.video.title, 'Test Video')
        self.assertEqual(self.video.description, 'Test Description')
        self.assertEqual(self.video.url, 'https://www.youtube.com/watch?v=9bZkp7q19f0')
    
class CategoryModelTestCase(TestCase):

    def setUp(self):
        self.category = Category(title='Test Category', color='#000000')

    def test_category_str(self):
        self.assertEqual(self.category.title, 'Test Category')
        self.assertEqual(self.category.color, '#000000')