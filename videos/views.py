from rest_framework import viewsets, generics, filters
from videos.models import Video, Category
from videos.serializer import VideoSerializer, CategorySerializer, VideosByCategorySerializer

class VideosViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class VideosByCategoryViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Video.objects.filter(category=self.kwargs['pk'])
        return queryset
    serializer_class = VideosByCategorySerializer