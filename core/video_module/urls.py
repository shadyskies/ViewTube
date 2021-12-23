from django.urls import path
from .views import home, VideoAPIList

urlpatterns = [
    path('', home, name='home'),
    path('api/videolist/', VideoAPIList.as_view(), name='api_videolist')
]