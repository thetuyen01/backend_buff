from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Sticky
from .serializers import StickySerializers

class StickyView(APIView):
    def get(self, request):
        position = request.GET.get('position', None)
        stickies = Sticky.objects.filter(position=position).first()
        serializers = StickySerializers(stickies)
        return Response(serializers.data, status=status.HTTP_200_OK)