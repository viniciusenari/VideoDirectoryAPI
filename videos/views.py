from rest_framework import viewsets, generics, filters
from videos.models import Video, Category
from videos.serializer import VideoSerializer, CategorySerializer, VideosByCategorySerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class VideosViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.get_queryset().order_by('id')
    serializer_class = VideoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.get_queryset().order_by('id')
    serializer_class = CategorySerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class VideosByCategoryViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Video.objects.filter(category=self.kwargs['pk'])
        return queryset
    serializer_class = VideosByCategorySerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class FreeVideosViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Video.objects.order_by("-id")[:10]
        return queryset
    serializer_class = VideoSerializer