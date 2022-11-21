from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions

from videos.views import VideosViewSet, CategoriesViewSet, VideosByCategoryViewSet, FreeVideosViewSet

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Videos API",
      default_version='v1',
      description="API for videos and categories",
      terms_of_service="#",
      contact=openapi.Contact(email="#"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


router = routers.DefaultRouter()
router.register('videos', VideosViewSet, basename='Videos')
router.register('categories', CategoriesViewSet, basename='Categories')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('categories/<int:pk>/videos/', VideosByCategoryViewSet.as_view()),
    path('videos/free', FreeVideosViewSet.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
