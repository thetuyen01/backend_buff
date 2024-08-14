from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Video
from .serializers import VideoSerializers 

class VideoView(APIView):
    def get(self, request):
        search = request.GET.get('search', None)
        pageSize = request.GET.get('pageSize', 10)  # Mặc định là 10 nếu không được chỉ định
        pageIndex = request.GET.get('pageIndex', 1)  # Mặc định là trang 1 nếu không được chỉ định
        try:
            pageSize = int(pageSize)
            pageIndex = int(pageIndex)
        except ValueError:
            return Response({'error': 'pageSize and page number must be valid integers.'}, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = Video.objects.filter()

        if search:
            queryset = queryset.filter(Q(title__icontains=search) | Q(description__icontains=search))

        paginator = Paginator(queryset.order_by('id'), per_page=pageSize)
        
        try:
            page = paginator.page(pageIndex)
            serializer = VideoSerializers(page.object_list, many=True)
            data_to_cache = {
                'data': serializer.data,
                'pageSize': pageSize,
                'pageIndex': pageIndex,
                'total': queryset.count()
            }
            return Response(data_to_cache, status=status.HTTP_200_OK)
        except (PageNotAnInteger, EmptyPage):
            return Response({
                'data': [],
                'pageSize': pageSize,
                'pageIndex': pageIndex,
                'total': queryset.count() 
            }, status=status.HTTP_200_OK)
