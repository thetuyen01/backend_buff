from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q, Value, CharField
from .models import Video
from categories.models import Category
from .serializers import VideoSerializers
from django.shortcuts import get_object_or_404
import random
from django.db.models.functions import Concat
from unidecode import unidecode

class VideoView(APIView):
    def get(self, request):
        categoriesSlug = request.query_params.get('search[params][categoriesSlug]')
        search = request.query_params.get('search[params][search]')
        pageSize = request.query_params.get('search[params][pageSize]')
        pageIndex = request.query_params.get('search[params][pageIndex]')
        topSearch = request.query_params.get('search[params][topSearch]')

        # Validate pageSize and pageIndex
        try:
            pageSize = int(pageSize)
            pageIndex = int(pageIndex)
        except ValueError:
            return Response({'error': 'pageSize and pageIndex must be valid integers.'}, status=status.HTTP_400_BAD_REQUEST)

        # Build the queryset based on filters
        queryset = Video.objects.all()

        if topSearch:
            search = topSearch.replace('-', ' ')
            categoriesSlug = None

        if search:
            normalized_search = unidecode(search).lower()
            queryset = queryset.annotate(
                title_no_diacritics=Concat(Value(""), 'title_no_unidecode', output_field=CharField()),
                description_no_diacritics=Concat(Value(""), 'description', output_field=CharField())
            ).filter(
                Q(title_no_diacritics__icontains=normalized_search) |
                Q(description_no_diacritics__icontains=normalized_search)
            )

        if categoriesSlug:
            category = Category.objects.filter(slug=categoriesSlug).first()
            if not category:
                # Get a random category if no match is found
                category = random.choice(Category.objects.all())
            queryset = queryset.filter(category__id=category.id)

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