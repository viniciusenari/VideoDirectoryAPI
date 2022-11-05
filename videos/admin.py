from django.contrib import admin
from videos.models import Video

class Videos(admin.ModelAdmin):
    list_display = ('title', 'description', 'url')
    list_display_links = ('title', 'description', 'url')

admin.site.register(Video, Videos)

class Categories(admin.ModelAdmin):
    list_display = ('title', 'color')
    list_display_links = ('title', 'color')