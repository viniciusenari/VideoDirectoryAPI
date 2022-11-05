from django.contrib import admin
from django.urls import path, include
from videos.views import VideosViewSet, CategoriesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('videos', VideosViewSet, basename='Videos')
router.register('categories', CategoriesViewSet, basename='Categories')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
