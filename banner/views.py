from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Banner
from .serializers import BannerSerializers

class BannerView(APIView):
    def get(self, request):
        sz_banners = BannerSerializers(Banner.objects.all(), many=True)
        return Response(sz_banners.data, status=status.HTTP_200_OK)