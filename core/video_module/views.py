from django.shortcuts import render
from .models import YoutubeVideo
import asyncio
from .utils import get_videos_async
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import VideoListSerializer

def home(request):
    videos = YoutubeVideo.objects.all()
    context = {
        'videos': videos,
    }
    # run get videos async
    # get_videos_async('cricket')
    return render(request, 'video_module/home.html', context)


# api to get videos from Youtube search API ordered by published date (most recent first)
class VideoAPIList(ListAPIView):
    # permission_classes = (AllowAny,)
    serializer_class = VideoListSerializer
    queryset = YoutubeVideo.objects.all()

    def get(self, request, *args, **kwargs):
        # get queryset ordered by published date
        qs = YoutubeVideo.objects.all().order_by('-published_at')
        # serialize objs
        page = self.paginate_queryset(qs)
        ser = VideoListSerializer(page, many=True)
        return self.get_paginated_response(ser.data)