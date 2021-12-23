from dotenv import load_dotenv
import requests
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from django.utils import timezone


from video_module.models import YoutubeVideo
# get videos from Youtube search API ordered by published date (most recent first)
# def get_videos(search:str):
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

# async function to get videos from Youtube search API ordered by published date (most recent first)
def run():
    print(f"running script for getting videos:: {timezone.now()}")
    # search query
    search = "cricket"
    load_dotenv()
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=os.getenv('YOUTUBE_API_KEY'))

  # Call the search.list method to retrieve results matching the specified
  # query term.
    search_response = youtube.search().list(
            q=search,
            part='id,snippet',
            maxResults=10, 
            order='date',
    ).execute()

    # create YoutubeVideo objects from search results and store in db
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            # create if same id does not exists
            if YoutubeVideo.objects.filter(video_id=search_result['id']['videoId']).count() == 0:
                video = YoutubeVideo(
                        title=search_result['snippet']['title'],
                        description=search_result['snippet']['description'],
                        published_at=search_result['snippet']['publishedAt'],
                        thumbnail_url=search_result['snippet']['thumbnails']['default']['url'],
                        video_id=search_result['id']['videoId']
                )
                video.save()
