from rest_framework import viewsets, generics, filters
from videos.models import Video, Category
from videos.serializer import VideoSerializer, CategorySerializer, VideosByCategorySerializer

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class VideosViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.get_queryset().order_by('id')
    serializer_class = VideoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    @method_decorator(cache_page(60 * 15))
    def dispatch(self, *args, **kwargs):
        return super(VideosViewSet, self).dispatch(*args, **kwargs)

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.get_queryset().order_by('id')
    serializer_class = CategorySerializer

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    @method_decorator(cache_page(60 * 15))
    def dispatch(self, *args, **kwargs):
        return super(CategoriesViewSet, self).dispatch(*args, **kwargs)

class VideosByCategoryViewSet(generics.ListAPIView):

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Video.objects.none()

        queryset = Video.objects.filter(category_id=self.kwargs['pk'])
        return queryset

    serializer_class = VideosByCategorySerializer

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

class FreeVideosViewSet(generics.ListAPIView):
    def get_queryset(self):
        # query 10 videos
        queryset = Video.objects.filter(category_id=1)
        return queryset
    serializer_class = VideoSerializer

    throttle_classes = [UserRateThrottle, AnonRateThrottle]