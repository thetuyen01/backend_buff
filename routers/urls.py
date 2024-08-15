from django.urls import path
from categories.views import CategoryView
from banner.views import BannerView
from videos.views import VideoView, VideoDetailView
from sticky.views import StickyView
from search.views import SearchView
urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('banners/', BannerView.as_view()),
    path('videos/', VideoView.as_view()),
    path('videos/detail/<str:slug>/', VideoDetailView.as_view()),
    path('stickies/', StickyView.as_view()),
    path('search/', SearchView.as_view())
]