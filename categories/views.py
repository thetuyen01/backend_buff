from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from .serializers import CategorySerializers
class CategoryView(APIView):
    def get(self, request):
        sz_categories = CategorySerializers(Category.objects.all(), many=True)
        return Response(sz_categories.data, status=status.HTTP_200_OK)