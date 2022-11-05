from rest_framework import viewsets
from videos.models import Video, Category
from videos.serializer import VideoSerializer, CategorySerializer

class VideosViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    
class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer