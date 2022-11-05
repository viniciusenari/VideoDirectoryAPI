from rest_framework import viewsets
from videos.models import Video
from videos.serializer import VideoSerializer

class VideosViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer