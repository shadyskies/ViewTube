from django.shortcuts import render
from .models import YoutubeVideo
import asyncio
from .utils import get_videos_async

def home(request):
    videos = YoutubeVideo.objects.all()
    context = {
        'videos': videos,
    }
    # run get videos async
    get_videos_async('cricket')
    return render(request, 'video_module/home.html', context)
