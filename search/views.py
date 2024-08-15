from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Search
from .serializers import SearchSerializers

class SearchView(APIView):
    def get(self, request):
        searches = Search.objects.all()
        searches = SearchSerializers(searches, many=True)
        return Response(searches.data, status=status.HTTP_200_OK)
