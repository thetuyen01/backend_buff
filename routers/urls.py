from django.urls import path
from categories.views import CategoryView
from banner.views import BannerView
from videos.views import VideoView
urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('banners/', BannerView.as_view()),
    path('videos/', VideoView.as_view()),
]