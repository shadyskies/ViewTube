from rest_framework.serializers import ModelSerializer
from .models import YoutubeVideo


class VideoListSerializer(ModelSerializer):
    class Meta:
        model = YoutubeVideo
        fields = "__all__"
