from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from .models import Video
from categories.models import Category
from .serializers import VideoSerializers
from django.shortcuts import get_object_or_404

class VideoView(APIView):
    def get(self, request):
        categoriesSlug = request.GET.get('categoriesSlug', None)
        search = request.GET.get('search', None)
        pageSize = request.GET.get('pageSize', 10)
        pageIndex = request.GET.get('pageIndex', 1)

        # Validate pageSize and pageIndex
        try:
            pageSize = int(pageSize)
            pageIndex = int(pageIndex)
        except ValueError:
            return Response({'error': 'pageSize and pageIndex must be valid integers.'}, status=status.HTTP_400_BAD_REQUEST)

        # Build the queryset based on filters
        queryset = Video.objects.all()
        if search:
            queryset = queryset.filter(Q(title__icontains=search) | Q(description__icontains=search))
        if categoriesSlug:
            categories = Category.objects.filter(slug=categoriesSlug).first()
            queryset = queryset.filter(category__id=categories.id)  # Corrected field name

        # Check if the queryset is empty after filtering
        if not queryset.exists():
            return Response({
                'data': [],
                'pageSize': pageSize,
                'pageIndex': pageIndex,
                'total': 0
            }, status=status.HTTP_200_OK)

        # Paginate the queryset
        paginator = Paginator(queryset.order_by('id'), per_page=pageSize)
        try:
            page = paginator.page(pageIndex)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)  # Handle the case where pageIndex is out of range

        # Serialize the data
        serializer = VideoSerializers(page.object_list, many=True)
        data_to_cache = {
            'data': serializer.data,
            'pageSize': pageSize,
            'pageIndex': pageIndex,
            'total': paginator.count
        }
        return Response(data_to_cache, status=status.HTTP_200_OK)

class VideoDetailView(APIView):
    def get(self, request, slug):
        video = get_object_or_404(Video, slug=slug)
        serializer = VideoSerializers(video)
        return Response(serializer.data, status=status.HTTP_200_OK)