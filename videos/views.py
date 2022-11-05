from rest_framework import viewsets, generics
from videos.models import Video, Category
from videos.serializer import VideoSerializer, CategorySerializer, VideosByCategorySerializer

class VideosViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class VideosByCategoryViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Video.objects.filter(category=self.kwargs['pk'])
        return queryset
    serializer_class = VideosByCategorySerializer