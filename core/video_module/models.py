from django.db import models

# store Youtube videos
class YoutubeVideo(models.Model):
    video_id  = models.CharField(max_length=100)
    title = models.CharField(max_length=512)
    description = models.CharField(max_length=1024)
    channel_title = models.CharField(max_length=512)
    thumbnail_url = models.CharField(max_length=512)
    published_at = models.DateTimeField()

