from django.db import models

class Video(models.Model):
    category = models.ForeignKey('Category', default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=20)
    color = models.CharField(max_length=7)