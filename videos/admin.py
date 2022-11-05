from django.contrib import admin
from videos.models import Video

class Videos(admin.ModelAdmin):
    list_display = ('title', 'description', 'url')
    list_display_links = ('title', 'description', 'url')

admin.site.register(Video, Videos)